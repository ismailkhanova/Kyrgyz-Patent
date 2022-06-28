from django.views.generic import ListView, DetailView, View, FormView
from django.shortcuts import render
from .models import IpMark
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


class MarkDetail(DetailView):
    model = IpMark
    template_name = 'mark_detail.html'
    context_object_name = "mark"



