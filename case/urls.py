from django.urls import path

from .views import (add_witness_to_case,
                    ajax_add_witness_to_case,ajax_delete_witness_to_case,CaseUpdateView)

urlpatterns = [

    path('<int:pk>', add_witness_to_case, name='add_witness_to_case'),
    path('update/<int:pk>', CaseUpdateView.as_view(), name='case_update'),
    path('<int:pk>/witness/<int:id>', ajax_add_witness_to_case, name='ajax_add_witness_to_case'),
    path('<int:pk>/remove/<int:id>', ajax_delete_witness_to_case, name='ajax_delete_witness_to_case'),

]
