from django.views.generic import ListView, DetailView, View, FormView
from django.shortcuts import render
from .models import IpMark, TblTims, TblNmpt, TblAvtor, TblSp, TblOtz, TblBd, TblInv, TblPm, TblPobr, TblEvm, TblCel, TblTrz, TblRp, License
from django.db.models import Q


class MarkSearchView(ListView):
    model = IpMark
    template_name = 'marks_search.html'
    context_object_name = 'marks'


class MarkSearchResultView(ListView):
    model = IpMark
    template_name = 'marks_search_result.html'
    context_object_name = 'mark_result'
    paginate_by = 20


    def get_queryset(self):  # новый
        reg = self.request.GET.get('reg')
        name = self.request.GET.get('name')
        rdate = self.request.GET.get('rdate')
        exp = self.request.GET.get('exp')
        nbr = self.request.GET.get('nbr')
        mktu = self.request.GET.get('mktu')
        fdate = self.request.GET.get('fdate')
        owner = self.request.GET.get('owner')
        mark_result = IpMark.objects.filter(
            Q(registration_date__icontains=rdate) & Q(mark_name__icontains=name) &
            Q(expiration_date__icontains=exp) & Q(txt_nice_class_code__icontains=mktu) &
            Q(registration_nbr__icontains=reg) & Q(file_nbr__icontains=nbr) &
            Q(filing_date__icontains=fdate) & Q (owner_name__icontains=owner)
        )

        return mark_result

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reg'] = self.request.GET.get('reg')
    #     context['name'] = self.request.GET.get('name')
    #     context['rdate'] = self.request.GET.get('rdate')
    #     context['exp'] = self.request.GET.get('exp')
    #     context['nbr'] = self.request.GET.get('nbr')
    #     context['mktu'] = self.request.GET.get('mktu')
    #     context['fdate'] = self.request.GET.get('fdate')
    #     context['owner'] = self.request.GET.get('owner')
    #     return context


class MarkDetail(DetailView):
    model = IpMark
    template_name = 'mark_detail.html'
    context_object_name = "mark"


class TimsSearchView(ListView):
    model = TblTims
    template_name = 'tims_search.html'
    context_object_name = 'tims'


class TimsSearchResultView(ListView):
    model = TblTims
    template_name = 'tims_search_result.html'
    context_object_name = 'tims_result'
    paginate_by = 20

    def get_queryset(self):  # новый
        nbrs = self.request.GET.get('nbrs')
        rdate = self.request.GET.get('rdate')
        nreg = self.request.GET.get('nreg')
        nbr = self.request.GET.get('nbr')
        indate = self.request.GET.get('indate')
        name = self.request.GET.get('name')
        app = self.request.GET.get('app')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        tims_result = TblTims.objects.filter(
            Q(num_svid_t__icontains=nbrs) & Q(date_svid_t__icontains=rdate) &
            Q(number_reg_t__icontains=nreg) & Q(in_date_t__icontains=indate) &
            Q(name_t__icontains=name) & Q(app_t__icontains=app) &
            Q(avtor_t__icontains=avt) & Q (owner_t__icontains=owner)
        )

        return tims_result

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['nbrs'] = self.request.GET.get('nbrs')
    #     context['rdate'] = self.request.GET.get('rdate')
    #     context['nreg'] = self.request.GET.get('nreg')
    #     context['nbr'] = self.request.GET.get('nbr')
    #     context['indate'] = self.request.GET.get('indate')
    #     context['name'] = self.request.GET.get('name')
    #     context['app'] = self.request.GET.get('app')
    #     context['avt'] = self.request.GET.get('avt')
    #     context['owner'] = self.request.GET.get('owner')
    #     return context


class TimsDetail(DetailView):
    model = TblTims
    template_name = 'tims_detail.html'
    context_object_name = "tims"


class NmptSearchView(ListView):
    model = TblNmpt
    template_name = 'nmpt_search.html'
    context_object_name = 'nmpt'


class NmptSearchResultView(ListView):
    model = TblNmpt
    template_name = 'nmpt_search_results.html'
    context_object_name = 'nmpt_result'
    paginate_by = 20

    def get_queryset(self):  # новый
        nbrs = self.request.GET.get('nbrs')
        rdate = self.request.GET.get('rdate')
        exp = self.request.GET.get('exp')
        fdate = self.request.GET.get('fdate')
        name = self.request.GET.get('name')
        owner = self.request.GET.get('owner')
        vid = self.request.GET.get('vid')
        nmpt_result = TblNmpt.objects.filter(
            Q(k11__icontains=nbrs) & Q(k15__icontains=rdate) & Q(k18__icontains=exp)
            & Q(k22__icontains=fdate) & Q(k54__icontains=name) &
            Q(k73__icontains=owner) & Q(k73__icontains=name) & Q(vid_tovara__icontains=vid)
        )

        return nmpt_result

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['nbrs'] = self.request.GET.get('nbrs')
    #     context['rdate'] = self.request.GET.get('rdate')
    #     context['exp'] = self.request.GET.get('exp')
    #     context['fdate'] = self.request.GET.get('fdate')
    #     context['name'] = self.request.GET.get('name')
    #     context['owner'] = self.request.GET.get('owner')
    #     context['vid'] = self.request.GET.get('vid')
    #     return context


class NmptDetailView(DetailView):
    model = TblNmpt
    template_name = 'nmpt_detail.html'
    context_object_name = 'nmpt'


class AvtorSearchView(ListView):
    model = TblAvtor
    template_name = 'avtor_search.html'
    context_object_name = 'avtor'


class AvtorSearchResultView(ListView):
    model = TblAvtor
    template_name = 'avtor_search_result.html'
    context_object_name = 'avtor_result'
    paginate_by = 20

    def get_queryset(self):
        inum = self.request.GET.get('inum')
        regn = self.request.GET.get('regn')
        rnum = self.request.GET.get('rnum')
        indate = self.request.GET.get('indate')
        avt = self.request.GET.get('avt')
        nwork = self.request.GET.get('nwork')
        owner = self.request.GET.get('owner')
        iden = self.request.GET.get('iden')
        avtor_result = TblAvtor.objects.filter(
            Q(in_number__icontains=inum) & Q(registration_number__icontains=regn) &
            Q(regist_number__icontains=rnum) & Q(in_date__icontains=indate) &
            Q(avtor__icontains=avt) & Q(name_work__icontains=nwork) &
            Q(owner__icontains=owner) & Q(iden__icontains=iden)
        )

        return avtor_result


class AvtorDetailView(DetailView):
    model = TblAvtor
    template_name = 'avtor_detail.html'
    context_object_name = 'avtor'


class SpSearchView(ListView):
    model = TblSp
    template_name = 'sp_search.html'
    context_object_name = 'sp'


class SpSearchResultView(ListView):
    model = TblSp
    template_name = 'sp_search_result.html'
    context_object_name = 'sp_result'
    paginate_by = 20

    def get_queryset(self):
        nums = self.request.GET.get('nums')
        rdate = self.request.GET.get('rdate')
        rnum = self.request.GET.get('rnum')
        indate = self.request.GET.get('indate')
        name = self.request.GET.get('name')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        sp_result = TblSp.objects.filter(
            Q(number_svid__icontains=nums) & Q(date_svid__icontains=rdate) &
            Q(registration_number__icontains=rnum) & Q(in_date__icontains=indate) &
            Q(name_object__icontains=name) & Q(object_name_use__icontains=avt) &
            Q(owner_imushest_prav__icontains=owner)
        )

        return sp_result


class SpDetailView(DetailView):
    model = TblSp
    template_name = 'sp_detail.html'
    context_object_name = 'sp'


class OtzSearchView(ListView):
    model = TblOtz
    template_name = 'otz_search.html'
    context_object_name = 'otz'


class OtzSearchResultView(ListView):
    model = TblOtz
    template_name = 'otz_search_result.html'
    context_object_name = 'otz_result'
    paginate_by = 20

    def get_queryset(self):
        nums = self.request.GET.get('nums')
        rdate = self.request.GET.get('rdate')
        otz = self.request.GET.get('otz')
        otz_result = TblOtz.objects.filter(
            Q(k11__icontains=nums) & Q(k15__icontains=rdate) &
            Q(k54__icontains=otz)
        )

        return otz_result


class OtzDetailView(DetailView):
    model = TblOtz
    template_name = 'otz_detail.html'
    context_object_name = 'otz'


class BdSearchView(ListView):
    model = TblBd
    template_name = 'bd_search.html'
    context_object_name = 'bd'


class BdSearchResultView(ListView):
    model = TblBd
    template_name = 'bd_search_result.html'
    context_object_name = 'bd_result'
    paginate_by = 20

    def get_queryset(self):
        nums = self.request.GET.get('nums')
        rdate = self.request.GET.get('rdate')
        rnum = self.request.GET.get('rnum')
        indate = self.request.GET.get('indate')
        name = self.request.GET.get('name')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        bd_result = TblBd.objects.filter(
            Q(num_svid__icontains=nums) & Q(date_svid__icontains=rdate) &
            Q(number_reg__icontains=rnum) & Q(in_date__icontains=indate) &
            Q(name__icontains=name) & Q(avtor__icontains=avt) &
            Q(owner__icontains=owner)
        )

        return bd_result


class BdDetailView(DetailView):
    model = TblBd
    template_name = 'bd_detail.html'
    context_object_name = 'bd'


class InvSearchView(ListView):
    model = TblInv
    template_name = 'inv_search.html'
    context_object_name = 'inv'


class InvSearchResultView(ListView):
    model = TblInv
    template_name = 'inv_search_result.html'
    context_object_name = 'inv_result'
    paginate_by = 20

    def get_queryset(self):
        num = self.request.GET.get('num')
        rdate = self.request.GET.get('rdate')
        mpk = self.request.GET.get('mpk')
        name = self.request.GET.get('name')
        app = self.request.GET.get('app')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        inv_result = TblInv.objects.filter(
            Q(f210__icontains=num) & Q(f150__icontains=rdate) &
            Q(f510__icontains=mpk) & Q(f540__icontains=name) &
            Q(f731__icontains=app) & Q(f732__icontains=avt) &
            Q(f733__icontains=owner)
        )

        return inv_result


class InvDetailView(DetailView):
    model = TblInv
    template_name = 'inv_detail.html'
    context_object_name = 'inv'


class PmSearchView(ListView):
    model = TblPm
    template_name = 'pm_search.html'
    context_object_name = 'pm'


class PmSearchResultView(ListView):
    model = TblPm
    template_name = 'pm_search_result.html'
    context_object_name = 'pm_result'
    paginate_by = 20

    def get_queryset(self):
        num = self.request.GET.get('num')
        rdate = self.request.GET.get('rdate')
        mpk = self.request.GET.get('mpk')
        name = self.request.GET.get('name')
        app = self.request.GET.get('app')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        pm_result = TblPm.objects.filter(
            Q(f210__icontains=num) & Q(f150__icontains=rdate) &
            Q(f510__icontains=mpk) & Q(f540__icontains=name) &
            Q(f731__icontains=app) & Q(f732__icontains=avt) &
            Q(f733__icontains=owner)
        )

        return pm_result


class PmDetailView(DetailView):
    model = TblPm
    template_name = 'pm_detail.html'
    context_object_name = 'pm'


class PobrSearchView(ListView):
    model = TblPobr
    template_name = 'pobr_search.html'
    context_object_name = 'pobr'

class PobrSearchResultView(ListView):
    model = TblPobr
    template_name = 'pobr_search_result.html'
    context_object_name = 'pobr_result'
    paginate_by = 20

    def get_queryset(self):
        num = self.request.GET.get('num')
        rdate = self.request.GET.get('rdate')
        mkpo = self.request.GET.get('mkpo')
        name = self.request.GET.get('name')
        app = self.request.GET.get('app')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        pobr_result = TblPobr.objects.filter(
            Q(f210__icontains=num) & Q(f150__icontains=rdate) &
            Q(f510__icontains=mkpo) & Q(f540__icontains=name) &
            Q(f731__icontains=app) & Q(f732__icontains=avt) &
            Q(f733__icontains=owner)
        )

        return pobr_result


class PobrDetailView(DetailView):
    model = TblPobr
    template_name = 'pobr_detail.html'
    context_object_name = 'pobr'


class EvmSearchView(ListView):
    model = TblEvm
    template_name = 'evm_search.html'
    context_object_name = 'evm'


class EvmSearchResultView(ListView):
    model = TblEvm
    template_name = 'evm_search_result.html'
    context_object_name = 'evm_result'
    paginate_by = 20

    def get_queryset(self):
        nums = self.request.GET.get('nums')
        rdate = self.request.GET.get('rdate')
        rnum = self.request.GET.get('rnum')
        indate = self.request.GET.get('indate')
        nwork = self.request.GET.get('nwork')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        evm_result = TblEvm.objects.filter(
            Q(number_svid__icontains=nums) & Q(date_svid__icontains=rdate) &
            Q(registration_number__icontains=rnum) & Q(in_date__icontains=indate) &
            Q(avtor__icontains=avt) & Q(name_work__icontains=nwork) &
            Q(owner__icontains=owner)
        )

        return evm_result


class EvmDetailView(DetailView):
    model = TblEvm
    template_name = 'evm_detail.html'
    context_object_name = 'evm'


class CelSearchView(ListView):
    model = TblCel
    template_name = 'cel_search.html'
    context_object_name = 'cel'


class CelSearchResultView(ListView):
    model = TblCel
    template_name = 'cel_search_result.html'
    context_object_name = 'cel_result'
    paginate_by = 20

    def get_queryset(self):
        num = self.request.GET.get('num')
        rdate = self.request.GET.get('rdate')
        rnum = self.request.GET.get('rnum')
        name = self.request.GET.get('name')
        rus = self.request.GET.get('rus')
        lat = self.request.GET.get('lat')
        app = self.request.GET.get('app')
        avt = self.request.GET.get('avt')
        owner = self.request.GET.get('owner')
        cel_result = TblCel.objects.filter(
            Q(f210__icontains=num) & Q(f150__icontains=rdate) &
            Q(f100__icontains=rnum) & Q(f540__icontains=name) &
            Q(f600__icontains=rus) & Q(f601__icontains=lat) &
            Q(f731__icontains=app) & Q(f732__icontains=avt) &
            Q(f733__icontains=owner)
        )

        return cel_result


class CelDetailView(DetailView):
    model = TblCel
    template_name = 'cel_detail.html'
    context_object_name = 'cel'


class TrzSearchView(ListView):
    model = TblTrz
    template_name = 'trz_search.html'
    context_object_name = 'trz'


class TrzSearchResultView(ListView):
    model = TblTrz
    template_name = 'trz_search_result.html'
    context_object_name = 'trz_result'
    paginate_by = 20

    def get_queryset(self):
        inum = self.request.GET.get('inum')
        rdate = self.request.GET.get('rdate')
        nums = self.request.GET.get('nums')
        name = self.request.GET.get('name')
        app = self.request.GET.get('app')
        trz_result = TblTrz.objects.filter(
            Q(in_number__icontains=inum) & Q(number_svid__icontains=nums) &
            Q(data_svid__icontains=rdate) & Q(nametrz_ru__icontains=name) &
            Q(zayavitel__icontains=app)
        )

        return trz_result


class TrzDetailView(DetailView):
    model = TblTrz
    template_name = 'trz_detail.html'
    context_object_name = 'trz'


class RpSearchView(ListView):
    model = TblRp
    template_name = 'rp_search.html'
    context_object_name = 'rp'


class RpSearchResultView(ListView):
    model = TblRp
    template_name = 'rp_search_result.html'
    context_object_name = 'rp_result'
    paginate_by = 20

    def get_queryset(self):
        inum = self.request.GET.get('inum')
        indate = self.request.GET.get('indate')
        name = self.request.GET.get('name')
        regn = self.request.GET.get('regn')
        rdate = self.request.GET.get('rdate')
        avt = self.request.GET.get('avt')
        rp_result = TblRp.objects.filter(
            Q(f000__icontains=inum) & Q(f220__icontains=indate) &
            Q(f540__icontains=name) & Q(f100__icontains=regn) &
            Q(f150__icontains=rdate) & Q(f730__icontains=avt)
        )

        return rp_result


class RpDetailView(DetailView):
    model = TblRp
    template_name = 'rp_detail.html'
    context_object_name = 'rp'


class LicenseSearchView(ListView):
    model = License
    template_name = 'lic_search.html'
    context_object_name = 'lic'


class LicenseSearchResultView(ListView):
    model = License
    template_name = 'lic_search_result.html'
    context_object_name = 'lic_result'
    paginate_by = 20

    def get_queryset(self):
        numr = self.request.GET.get('numr')
        name = self.request.GET.get('name')
        rdate = self.request.GET.get('rdate')
        regn = self.request.GET.get('regn')
        licr = self.request.GET.get('licr')
        lict = self.request.GET.get('lict')
        lic_result = License.objects.filter(
            Q(in_number_lic__icontains=numr) & Q(name_ois__icontains=name) &
            Q(number_lic__icontains=regn) & Q(date_reg_lic__icontains=rdate) & Q(licensiar__icontains=licr)
            & Q(licensiat__icontains=lict)
        )

        return lic_result


class LicenseDetailView(DetailView):
    model = License
    template_name = 'lic_detail.html'
    context_object_name = 'lic'



















