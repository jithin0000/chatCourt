from django.urls import path

from .views import (EvidenceCrateView)

urlpatterns = [

    path('', EvidenceCrateView.as_view(), name='add_evidence'),

]
