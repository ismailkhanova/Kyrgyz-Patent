from django.urls import path
from .views import MarkSearchView, MarkSearchResultView, MarkDetail, \
    TimsSearchView, TimsSearchResultView, TimsDetail, \
    NmptSearchView, NmptSearchResultView, NmptDetailView, \
    AvtorSearchView, AvtorSearchResultView, AvtorDetailView, \
    SpSearchView, SpSearchResultView, SpDetailView, \
    OtzSearchView, OtzSearchResultView, OtzDetailView, \
    BdSearchView, BdSearchResultView, BdDetailView, \
    InvSearchView, InvSearchResultView, InvDetailView, \
    PmSearchView, PmSearchResultView, PmDetailView, \
    PobrSearchView, PobrSearchResultView, PobrDetailView, \
    EvmSearchView, EvmSearchResultView, EvmDetailView, \
    CelSearchView, CelSearchResultView, CelDetailView, \
    TrzSearchView, TrzSearchResultView, TrzDetailView, \
    RpSearchView, RpSearchResultView, RpDetailView, \
    LicenseSearchView, LicenseSearchResultView, LicenseDetailView

urlpatterns = [
    path("", MarkSearchView.as_view(), name="marks_search"),
    path("mark_search/", MarkSearchResultView.as_view(), name='marks_search_results'),
    path("mark/<int:pk>/", MarkDetail.as_view(), name="mark_detail"),

    path("tims/", TimsSearchView.as_view(), name="tims_search"),
    path("tims_search/", TimsSearchResultView.as_view(), name="tims_search_results"),
    path("tims/<int:pk>/", TimsDetail.as_view(), name="tims_detail"),

    path("nmpt/", NmptSearchView.as_view(), name="nmpt_search"),
    path("nmpt_search/", NmptSearchResultView.as_view(), name="nmpt_search_results"),
    path("nmpt/<int:pk>/", NmptDetailView.as_view(), name="nmpt_detail"),

    path("avtor/", AvtorSearchView.as_view(), name="avtor_search"),
    path("avtor_search/", AvtorSearchResultView.as_view(), name="avtor_search_results"),
    path("avtor/<int:pk>/", AvtorDetailView.as_view(), name="avtor_detail"),

    path("sp/", SpSearchView.as_view(), name="sp_search"),
    path("sp_search/", SpSearchResultView.as_view(), name="sp_search_results"),
    path("sp/<int:pk>/", SpDetailView.as_view(), name="sp_detail"),

    path("otz/", OtzSearchView.as_view(), name="otz_search"),
    path("otz_search/", OtzSearchResultView.as_view(), name="otz_search_results"),
    path("otz/<int:pk>/", OtzDetailView.as_view(), name="otz_detail"),

    path("bd/", BdSearchView.as_view(), name="bd_search"),
    path("bd_search/", BdSearchResultView.as_view(), name="bd_search_results"),
    path("bd/<int:pk>/", BdDetailView.as_view(), name="bd_detail"),

    path("inv/", InvSearchView.as_view(), name="inv_search"),
    path("inv_search/", InvSearchResultView.as_view(), name="inv_search_results"),
    path("inv/<int:pk>/", InvDetailView.as_view(), name="inv_detail"),

    path("pm/", PmSearchView.as_view(), name="pm_search"),
    path("pm_search/", PmSearchResultView.as_view(), name="pm_search_results"),
    path("pm/<int:pk>/", PmDetailView.as_view(), name="pm_detail"),

    path("pobr/", PobrSearchView.as_view(), name="pobr_search"),
    path("pobr_search/", PobrSearchResultView.as_view(), name="pobr_search_results"),
    path("pobr/<int:pk>/", PobrDetailView.as_view(), name="pobr_detail"),

    path("evm/", EvmSearchView.as_view(), name="evm_search"),
    path("evm_search/", EvmSearchResultView.as_view(), name="evm_search_results"),
    path("evm/<int:pk>/", EvmDetailView.as_view(), name="evm_detail"),

    path("cel/", CelSearchView.as_view(), name="cel_search"),
    path("cel_search/", CelSearchResultView.as_view(), name="cel_search_results"),
    path("cel/<int:pk>/", CelDetailView.as_view(), name="cel_detail"),

    path("trz/", TrzSearchView.as_view(), name="trz_search"),
    path("trz_search/", TrzSearchResultView.as_view(), name="trz_search_results"),
    path("trz/<int:pk>/", TrzDetailView.as_view(), name="trz_detail"),

    path("rp/", RpSearchView.as_view(), name="rp_search"),
    path("rp_search/", RpSearchResultView.as_view(), name="rp_search_results"),
    path("rp/<int:pk>/", RpDetailView.as_view(), name="rp_detail"),

    path("lic/", LicenseSearchView.as_view(), name="lic_search"),
    path("lic_search/", LicenseSearchResultView.as_view(), name="lic_search_results"),
    path("lic/<int:pk>/", LicenseDetailView.as_view(), name="lic_detail")
]

