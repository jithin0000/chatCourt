from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
# Create your views here.
from evidence.forms import EvidenceForm


class EvidenceCrateView(LoginRequiredMixin, CreateView):
    """ create view for evidence"""
    form_class = EvidenceForm
    template_name = 'evidence/create_evidence.html'
    success_url = "/home"