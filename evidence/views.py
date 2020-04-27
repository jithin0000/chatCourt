from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
# Create your views here.
from case.models import Case
from evidence.forms import EvidenceForCase, EvidenceCreateForm
from evidence.models import Evidence


class UpdateEvidence(LoginRequiredMixin, CreateView):
    """ create view for evidence"""
    form_class = EvidenceForCase

    def form_valid(self, form):
        form.instance.owner = self.request.user
        pk = self.kwargs.get("pk")
        case = get_object_or_404(Case, id=pk)
        form.instance.case = case
        return super().form_valid(form)
        # evidence.case
    def get_success_url(self):
        return reverse('lawyer_case_detail',kwargs={'pk':self.kwargs.get('pk')})

    template_name = 'evidence/create_evidence.html'


class CreateEvidence(LoginRequiredMixin, CreateView):
    """ create view for evidence"""
    form_class = EvidenceCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        pk = self.kwargs.get("pk")

        return super().form_valid(form)
        # evidence.case
    def get_success_url(self):
        return reverse('lawyer_evidence')

    template_name = 'evidence/create_evidence.html'


class EvidenceDetailView(LoginRequiredMixin, DetailView):
    """ create view for evidence"""
    model = Evidence
    template_name = "evidence/evidence_detail.html"

class EvidenceDeleteView(LoginRequiredMixin, DeleteView):
    """ create view for evidence"""
    model = Evidence
    template_name = 'evidence/evidence_delete.html'
    def get_success_url(self):
        return reverse('lawyer_evidence')



