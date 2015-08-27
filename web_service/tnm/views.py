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

def get_icds_neoplasm(request):

    icd_list_neoplasm = staging.tnm_neoplasms()


    request_data = {
        'request_status': 'success',
        'icd_list_neoplasm': icd_list_neoplasm,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_tnms(request, icd):

    ts_list = staging.tnm_t(icd)
    ns_list = staging.tnm_n(icd)
    ms_list = staging.tnm_m(icd)

    dukes_list = staging.tnm_dukes(icd)
    psa_list = staging.tnm_psa(icd)
    gleason_list = staging.tnm_gleason(icd)

    request_data = {
        'request_status': 'success',
        'ts_list': ts_list,
        'ns_list': ns_list,
        'ms_list': ms_list,
        'dukes_list': dukes_list,
        'psa_list': psa_list,
        'gleason_list': gleason_list,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')

def get_stage(request, icd, t, n, m, dukes=None, psa=None, gleason=None):

    if dukes!=None:
        stage = staging.tnm_stage(icd, t, n, m, dukes)

    stage = staging.tnm_stage(icd, t, n, m)
    stage1 = stage

    if stage1 == None:
        stage = 'Staging undefined'

    request_data = {
        'request_status': 'success',
        'stage': stage,
    }

    return HttpResponse(json.dumps(request_data), content_type='application/json')