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

    ts_list = staging.tnm_t(icd)
    ns_list = staging.tnm_n(icd)
    ms_list = staging.tnm_m(icd)

    request_data = {
        'request_status': 'success',
        'ts_list': ts_list,
        'ns_list': ns_list,
        'ms_list': ms_list
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_stage(request, icd, t, n, m):

    stage = staging.tnm_stage(icd, t, n, m)

    print stage
    request_data = {
        'request_status': 'success',
        'stage': stage,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')