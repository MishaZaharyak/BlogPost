from django.contrib import admin
from .forms import PostForm
from .models import PostModel, PostCommentModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "author", "is_owned_by_current_user", "get_created_at")
    form = PostForm
    request = None

    def get_queryset(self, request):
        self.request = request
        queryset = super().get_queryset(request).select_related('author')
        return queryset

    def is_owned_by_current_user(self, obj):
        return obj.author == self.request.user

    is_owned_by_current_user.short_description = "You owner"
    is_owned_by_current_user.boolean = True

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    get_created_at.short_description = "Created At"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True

        return request.user == obj.author

    def has_delete_permission(self, request, obj=None):
        if not obj:
            return True

        return request.user == obj.author


@admin.register(PostCommentModel)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', "author")

    def get_queryset(self, request):
        queryset = super().get_queryset(request).select_related('author', "post")
        return queryset
