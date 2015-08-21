from django import forms
from .models import Resultado, Cid, Tnm
from nedda.staging import corpus_uteri_sarcomas,lung, stomach,prostate, staging
from nedda.staging import breast, cervix_uteri,colon_rectum, corpus_uteri_carcinomas

ICD_CHOICES = breast.BREAST_CANCER_ICDS + cervix_uteri.CERVIX_UTERI_CANCER_ICDS \
              + colon_rectum.COLON_CANCER_ICDS + corpus_uteri_carcinomas.CORPUS_UTERI_CANCER_ICDS\
              + lung.LUNG_CANCER_ICDS + prostate.PROSTATE_CANCER_ICDS + stomach.STOMACH_CANCER_ICDS

class FormTnm(forms.ModelForm):
    t = forms.ChoiceField(widget=forms.Select)
    n = forms.ChoiceField(widget=forms.Select)
    m = forms.ChoiceField(widget=forms.Select)

class FormCid(forms.ModelForm):

    a = [('vazio', 'Escolha um CID')]
    for x in range(len(ICD_CHOICES)):
            a.append((str(x), ICD_CHOICES[x]))

    aux_t = [('vazio', 'Escolha um T')]
    aux_n = [('vazio', 'Escolha um N')]
    aux_m = [('vazio', 'Escolha um M')]

    cid = forms.ChoiceField(
        widget=forms.Select, choices=a, required=True )

    if cid in staging.BREAST_CANCER_ICDS:
        for x in range(len(staging.BreastCancerStager.BREAST_CANCER_TS)):
                aux_t.append((str(x), staging.BreastCancerStager.BREAST_CANCER_TS[x]))
        for x in range(len(staging.CervixUteriStager.CERVIX_UTERI_CANCER_NS)):
                aux_n.append((str(x), staging.BreastCancerStager.BREAST_CANCER_NS[x]))
        for x in range(len(staging.CervixUteriStager.CERVIX_UTERI_CANCER_MS)):
                aux_m.append((str(x), staging.BreastCancerStager.BREAST_CANCER_MS[x]))

    elif cid in staging.CERVIX_UTERI_CANCER_ICDS:
        for x in range(len(staging.CervixUteriStager.CERVIX_UTERI_CANCER_TS)):
                aux_t.append((str(x), staging.CervixUteriStager.CERVIX_UTERI_CANCER_TS[x]))
        for x in range(len(staging.CervixUteriStager.CERVIX_UTERI_CANCER_NS)):
                aux_n.append((str(x), staging.CervixUteriStager.CERVIX_UTERI_CANCER_NS[x]))
        for x in range(len(staging.CervixUteriStager.CERVIX_UTERI_CANCER_MS)):
                aux_m.append((str(x), staging.CervixUteriStager.CERVIX_UTERI_CANCER_MS[x]))

    elif cid in staging.COLON_CANCER_ICDS:
        for x in range(len(staging.ColonRectumStager.COLON_CANCER_TS)):
                aux_t.append((str(x), staging.ColonRectumStager.COLON_CANCER_TS[x]))
        for x in range(len(staging.ColonRectumStager.COLON_CANCER_NS)):
                aux_n.append((str(x), staging.ColonRectumStager.COLON_CANCER_NS[x]))
        for x in range(len(staging.ColonRectumStager.COLON_CANCER_MS)):
                aux_m.append((str(x), staging.ColonRectumStager.COLON_CANCER_MS[x]))
            # dukes = staging.ColonRectumStager.COLON_CANCER_DUKES

    elif cid in staging.CORPUS_UTERI_CANCER_ICDS:
        for x in range(len(staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_TS)):
                aux_t.append((str(x), staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_TS[x]))
        for x in range(len(staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_NS)):
                aux_n.append((str(x), staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_NS[x]))
        for x in range(len(staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_MS)):
                aux_m.append((str(x), staging.CorpusUteriSarcomaStager.CORPUS_UTERI_CANCER_MS[x]))
            # dukes = staging.CorpusUteriStager.CORPUS_UTERI_CANCER_DUKES

    elif cid in staging.LUNG_CANCER_ICDS:
        for x in range(len(staging.LungCancerStager.LUNG_CANCER_TS)):
                aux_t.append((str(x), staging.LungCancerStager.LUNG_CANCER_TS[x]))
        for x in range(len(staging.LungCancerStager.LUNG_CANCER_NS)):
                aux_n.append((str(x), staging.LungCancerStager.LUNG_CANCER_NS[x]))
        for x in range(len(staging.LungCancerStager.LUNG_CANCER_MS)):
                aux_m.append((str(x), staging.LungCancerStager.LUNG_CANCER_MS[x]))

    elif cid in staging.PROSTATE_CANCER_ICDS:
        for x in range(len(staging.ProstateCancerStager.PROSTATE_CANCER_TS)):
                aux_t.append((str(x), staging.ProstateCancerStager.PROSTATE_CANCER_TS[x]))
        for x in range(len(staging.ProstateCancerStager.PROSTATE_CANCER_NS)):
                aux_n.append((str(x), staging.ProstateCancerStager.PROSTATE_CANCER_NS[x]))
        for x in range(len(staging.ProstateCancerStager.PROSTATE_CANCER_MS)):
                aux_m.append((str(x), staging.ProstateCancerStager.PROSTATE_CANCER_MS[x]))

    else:
        for x in range(len(staging.StomachCancerStager.STOMACH_CANCER_TS)):
                aux_t.append((str(x), staging.StomachCancerStager.STOMACH_CANCER_TS[x]))
        for x in range(len(staging.StomachCancerStager.STOMACH_CANCER_NS)):
                aux_n.append((str(x), staging.StomachCancerStager.STOMACH_CANCER_NS[x]))
        for x in range(len(staging.StomachCancerStager.STOMACH_CANCER_MS)):
                aux_m.append((str(x), staging.StomachCancerStager.STOMACH_CANCER_MS[x]))


    t = forms.ChoiceField(widget=forms.Select, choices=aux_t)
    n = forms.ChoiceField(widget=forms.Select, choices=aux_n)
    m = forms.ChoiceField(widget=forms.Select, choices=aux_m)

    class Meta:
        # model = Cid
        model = Tnm
        model = Resultado
        fields = ('cid', 't', 'n', 'm', 'estagio')

