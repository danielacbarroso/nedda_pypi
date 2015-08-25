import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from nedda.staging.staging import GenericStager
#from .models import Cid, Tnm
from django.core import serializers
from nedda.staging.staging import STAGES
from nedda.staging import staging
import csv, os

icd_list_set = set()

def calcula(request):
    return render(request, "calcula.html")

def get_icds(request):

    icd_list = []
    if len(icd_list_set) == 0:

        for item in STAGES:
            icd_list_set.add(item['icd'])

        icd_list = list(icd_list_set)
        icd_list.sort()

    request_data = {
        'request_status': 'success',
        'icd_list': icd_list
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_tnms(request, icd):

    print icd
    ts_list = ['T1', 'T2', 'T3']
    ns_list = ['N1', 'M2', 'N3']
    ms_list = ['M0', 'M1']

    request_data = {
        'request_status': 'success',
        'ts_list': ts_list,
        'ns_list': ns_list,
        'ms_list': ms_list
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')