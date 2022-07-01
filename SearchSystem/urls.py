from django.urls import path
from .views import MarkSearchView, MarkSearchResultView, MarkDetail, \
    TimsSearchView, TimsSearchResultView, TimsDetail

urlpatterns = [
    path("", MarkSearchView.as_view(), name="marks_search"),
    path("mark_search/", MarkSearchResultView.as_view(), name='marks_search_results'),
    path("mark/<int:pk>/", MarkDetail.as_view(), name="mark_detail"),

    path("tims/", TimsSearchView.as_view(), name="tims_search"),
    path("tims_search/", TimsSearchResultView.as_view(), name="tims_search_results"),
    path("tims/<int:pk>/", TimsDetail.as_view(), name="tims_detail"),
]