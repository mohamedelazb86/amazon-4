from rest_framework.pagination import PageNumberPagination
class Mypaginations(PageNumberPagination):
    page_size=5
    