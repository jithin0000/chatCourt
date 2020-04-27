from django.urls import path

from .views import (UpdateEvidence, CreateEvidence, EvidenceDetailView, EvidenceDeleteView)

urlpatterns = [

    path('create/<int:pk>', UpdateEvidence.as_view(), name='add_evidence'),
    path('create', CreateEvidence.as_view(), name='create_evidence'),
    path('detail/<int:pk>', EvidenceDetailView.as_view(), name='evidence_detail'),
    path('delete/<int:pk>', EvidenceDeleteView.as_view(), name='evidence_delete'),

]
