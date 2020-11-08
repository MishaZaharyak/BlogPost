from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Count
from .forms import UserForm, VisitorForm
from .models import UserModel, VisitorModel

admin.site.unregister(Group)


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("get_full_name", 'email', "get_posts_count", "get_date_joined")
    form = UserForm

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(posts_count=Count('posts', distinct=True))
        return queryset

    def get_full_name(self, obj):
        return str(obj)

    get_full_name.short_description = "Name"

    def get_posts_count(self, obj):
        return obj.posts_count

    get_posts_count.short_description = "Posts count"

    def get_date_joined(self, obj):
        return obj.date_joined.strftime("%d.%m.%Y %H:%M")

    get_date_joined.short_description = "Date Joined"


@admin.register(VisitorModel)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("get_full_name", 'email')
    form = VisitorForm

    def get_full_name(self, obj):
        return str(obj)
