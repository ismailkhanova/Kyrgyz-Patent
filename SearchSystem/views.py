from django.views.generic import ListView, DetailView, View, FormView
from django.shortcuts import render
from .models import IpMark, TblTims
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg'] = self.request.GET.get('reg')
        context['name'] = self.request.GET.get('name')
        context['rdate'] = self.request.GET.get('rdate')
        context['exp'] = self.request.GET.get('exp')
        context['nbr'] = self.request.GET.get('nbr')
        context['mktu'] = self.request.GET.get('mktu')
        context['fdate'] = self.request.GET.get('fdate')
        context['owner'] = self.request.GET.get('owner')
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbrs'] = self.request.GET.get('nbrs')
        context['rdate'] = self.request.GET.get('rdate')
        context['nreg'] = self.request.GET.get('nreg')
        context['nbr'] = self.request.GET.get('nbr')
        context['indate'] = self.request.GET.get('indate')
        context['name'] = self.request.GET.get('name')
        context['app'] = self.request.GET.get('app')
        context['avt'] = self.request.GET.get('avt')
        context['owner'] = self.request.GET.get('owner')
        return context


class TimsDetail(DetailView):
    model = TblTims
    template_name = 'tims_detail.html'
    context_object_name = "tims"


