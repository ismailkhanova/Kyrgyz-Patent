from django.urls import path
from .views import MarkSearchView, MarkSearchResultView, MarkDetail

urlpatterns = [
    path("", MarkSearchView.as_view(), name="marks_search"),
    path("mark_search/", MarkSearchResultView.as_view(), name='marks_search_results'),
    path("mark/<int:pk>/", MarkDetail.as_view(), name="mark_detail"),
]