from rest_framework.response import Response
from rest_framework import viewsets, pagination
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from collections import OrderedDict
"""
class FasterPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.values('id').count()"""

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    #django_paginator_class = FasterPaginator
    """
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            #('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
    """
