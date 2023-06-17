from rest_framework.pagination import PageNumberPagination


class ApplicationsPagination(PageNumberPagination):
    page_size = 10
