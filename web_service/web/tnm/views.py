from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cid, Tnm
from .forms import FormCid, FormTnm
from django.core import serializers
from nedda.staging import lung, breast,cervix_uteri, staging


# Create your views here.
def index(request):
    lista_estadiamento = Cid.objects.all()
    return render(request, "lista.html",
        {'lista_estadiamento': lista_estadiamento})
    # return HttpResponse("Estadiamento TNM")

def calcula(request):
    t_breast = [()]
    if request.method == 'POST':
        form = FormCid(request.POST, request.FILES)
        form.cid = request.GET.get('cid')
        # if form.cid in staging.BREAST_CANCER_ICDS:
        #     t_breast = form.aux_t

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = FormCid()

    return render(request, "calcula.html", {'form': form})

def home(request):
    return render(request, 'home.html')

def estadiamento(request):
    tnm = Tnm.objects.all()
    retorno = serializers.serialize('json', tnm)
    return HttpResponse(retorno, 'mimetype="text/javascript')

# def filtrar_T(request):
#     t_breast = [[1, 'Tis'], [2, 'T0'], [3, 'T1']]
#     t_cervix = [(1,'T5'), (2, 'T7')]
#     t_lung = [(1, 'Ta'), (2, 'Tb')]
#
#     cid = request.GET.get('cid')
#
#     html = u'<option value="">Selecione</option>'
#     # if cid in staging.BREAST_CANCER_ICDS:
#     if cid == 'Breast':
#         for t in t_breast:
#             html = u'{0}<option value="{1}">{2}</option>'.format(html, t[0], t[1])
#     # elif cid in staging.CERVIX_UTERI_CANCER_ICDS:
#     elif cid == 'Cervix':
#         for t in t_cervix:
#             html = u'{0}<option value="{1}">{2}</option>'.format(html, t[0], t[1])
#     # elif cid in staging.LUNG_CANCER_ICDS:
#     elif cid == 'lung':
#         for t in t_lung:
#             html = u'{0}<option value="{1}">{2}</option>'.format(html, t[0], t[1])
#
#     return HttpResponse(html)