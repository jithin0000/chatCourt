from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic.edit import UpdateView
from case.models import Case
from customuser.models import MyUser
# Create your views here.

import json

class CaseUpdateView(UpdateView):
    """ update case """
    pass
@login_required(login_url="/")
def add_witness_to_case(request, pk):
    """ add witness to case"""
    case = get_object_or_404(Case, pk=pk)
    witnesses = MyUser.objects.filter(user_type='Witness').all()

    return render(request,'case/add_witness_to_case.html', {
        'case' : case,
        'witnesses' : witnesses
    })

@login_required()
def ajax_add_witness_to_case(request, pk, id):
    """ adding witness to case """
    case = get_object_or_404(Case, pk = pk)
    witness = get_object_or_404(MyUser, pk =id)

    message =""
    isAdded = False

    if witness in case.witness.all():
        isAdded = False
        message = "witness already in case"

    else:
        case.witness.add(witness)
        isAdded=True
        message = "Witness added"
    witness = model_to_dict(witness)

    return JsonResponse({
        "message" : message,
        "isAdded" : isAdded,
        "witness" : witness

    }, safe=False)



@login_required()
def ajax_delete_witness_to_case(request, pk, id):
    """ adding witness to case """
    case = get_object_or_404(Case, pk = pk)
    witness = get_object_or_404(MyUser, pk =id)

    isRemoved = False

    if witness in case.witness.all():
        case.witness.remove(witness)
        isRemoved = True

    return JsonResponse({
        "isRemoved" : isRemoved,

    }, safe=False)











