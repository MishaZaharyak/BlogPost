from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    """ provides custom paginate response """
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'number': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        }, status=200)

    def get_paginated_response_obj(self, data):
        """ provides paginated object """
        previous_page_number = self.page.previous_page_number() if self.page.has_previous() else None
        next_page_number = self.page.next_page_number() if self.page.has_next() else None

        return {
            'next_page_number': next_page_number,
            'previous_page_number': previous_page_number,
            "has_previous": self.page.has_previous(),
            'has_next': self.page.has_next(),
            'number': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        }
