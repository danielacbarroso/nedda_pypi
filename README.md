# Nedda
## Automatic TNM cancer staging library

**What is cancer?**

In layman terms, the truth is that the word *cancer* actually refers to a huge number
of different diseases. They have in common the fact that they are an abnormal 
reproduction of cells, and they have the capability to spread to other organs and parts 
of the body. The National Cancer Institute of the United States uses the interesting
expression "*a collection of related diseases*" to describe cancer[1].
  
Cancer can appear on almost animal tissue. On the human body, there are different
types of cancers for every organ and every kind of cell. To mention the most common
types in the US, in 2015 figures[2]:

|Cancer Type                                 | New Cases | Deaths  |
|--------------------------------------------|-----------|---------|
|Bladder                                     |	74,000   |  16,000 |
|Breast (Female)	                         | 231,840   |  40,290 |
|Breast (Male)       	                     |   2,350   |     440 |
|Colon and Rectal (Combined)	             | 132,700   |  49,700 |
|Endometrial	                             |  54,870   |  10,170 |
|Kidney (Renal Cell and Renal Pelvis) Cancer |	61,560   |  14,080 |
|Leukemia (All Types)	                     |  54,270   |  24,450 |
|Lung (Including Bronchus)	                 | 221,200   | 158,040 |
|Melanoma	                                 |  73,870   |   9,940 |
|Non-Hodgkin Lymphoma	                     |  71,850   |  19,790 |
|Pancreatic	                                 |  48,960   |  40,560 |
|Prostate	                                 | 220,800   |  27,540 |
|Thyroid	                                 |  62,450   |   1,950 |

**What is cancer staging?**

According to the introduction of the AJCC Cancer Staging Manual:

> "Cancer staging plays a pivotal role in the battle on cancer. It forms the basis for
> understanding the changes in population cancer incidence, extent of disease initial
> presentation, and the overall impact of improvements in cancer treatment. Staging
> forms the base for defining groups for inclusion in clinical trials. Most importantly,
> staging provides those with cancer and their physicians the critical benchmark for
> defining prognosis and the likelihood of overcoming the cancer and for determining
> the best treatment approach for their cases." [3]

Different types of cancer have completely different treatment options and prognostics
according to their staging. For instance, a very small and localized breast cancer
determines a certain treatment path and has a very good (more than 95%) chance of
total cure (or remission). Unfortunately, if the same type of cancer is not detected
early, it can grow and spread to the lymphatic system (local and distant) and to
other organs (metastatic disease). In this case, the treatment options are distinct,
and the chance of cure much more remote.

**How is cancer staged?**

There is a system called TNM to classify each kind cancer. It is maintained by the
international medical community, through an organization called UICC. For each type
of cancer there is a table that maps some values to a specific stage. Those values are
known as T - the size of the tumor, N - the affected regional nodes, and M - the presence
of metastatic disease. Some kinds of cancer can also consider other values on the computation. For
instance, to compute the stage for prostate cancer, it is also necessary to use the values of
PSA an Gleason. For Colon, a value known as Dukes.

The physician must know those values and manually look up on the specific table to correctly 
classify the cancer. Those tables are provided on medical manuals, and are updated periodicaly.

**How can Nedda help you?**

Nedda is a Python library that computes, given an ICD code and the T, N and M values, the resulting
staging. It is still a prototype. We intend to use Nedda in conjunction with a Oncology module we
have been developing for GNU Health [4], an open source and free (as in freedom and as in free beer
- GPL 3 rocks!) health administration system.

**How to use Nedda**

Nedda has still has a very simple interface. The idea is to pass to the library the ICD, T, N and M values
and get a stager object, that validates the input and computes the correct stage for different types of cancer:
```python
from nedda.staging.staging import tnm_stager_factory
stager = tnm_stager_factory('C50.0', 'T0', 'N1', 'M0')
```

As you can see, we have passed to a factory method the aforementioned inputs and we receive back a BreastCancerStager
object. It contains the following members:

stager.BREAST_CANCER_MS    stager.stage
stager.BREAST_CANCER_NS    stager.staging
stager.BREAST_CANCER_TS    stager.t
stager.icd                 stager.valid
stager.m                   stager.validate_tnm
stager.n                   stager.validation_message

If you call then:
```python
stager.stage
```

You will get the response:
```python
'IIA'
```

For the time being, that is pretty much that. Nedda works for breast, cervix uteri, colon and rectum 
and lung cancer. We are still working on prostate and stomach. We have published the repository here in 
such an imature state hoping that the community would give some architectural and functional ideas and, 
of course, contributions on coding!

**How does Nedda work?**

Nedda looks the ICD code and chooses from different lists which stager to return. Each cancer has a different 
table for TNM classification, so it is very difficult to be generic. Nedda, then, from different sets of 
regular expressions, matches the informed parameters to a determined stage. In the end, this is just a very 
fancy way to do a large number of nested 'ifs' and to code all those tables in a maintainable way.

Nedda also validates the Ts, Ns and Ms given to different lists according to the different cancer types. If an 
impossible combination is given, the TNM is considered invalid and a simple message is registered. We have
also made lots of tests.

Any ideas on how to do this complex set of nested ifs in a more elegant way is welcome! If you now arcane 
subjects such as graph theory, linear algebra, vector spaces, clustering and thinks that your knowledge can 
help us, please be my guest and "tell me what you have learned, because the questions run so deep for such 
a simple man" (Supertramp).
 
**Who is Nedda?**

Nedda Novaes is an Oncologist in Belo Horizonte, MG, Brazil. She currently works on a huge hospital 
called Santa Casa de Misericórdia de Minas Gerais, and deals mainly with public health and poor patients. 
She transcends the simple (yet extremely complex and dedication intensive) scientific and medical 
treatment of people. She really takes care of the social, psychological and human aspects of such a 
terrible disease, specially when associated to poverty and less than optimal social conditions. 
She was the inspiration to create this project and to work on such an arid and hermetic subject.
She also happens to be my mother!


[1] [What is Cancer](http://www.cancer.gov/about-cancer/what-is-cancer)
[2] American Cancer Society: Cancer Facts and Figures 2015. Atlanta, Ga: American Cancer Society, 2015. 
[3] Cancer Staging Handbook. From the AJCC Cancer Staging Manual. p. vii
[4] [GNU Health] (http://health.gnu.org/)

Copyright 2015 [Sílex Sistemas Ltda.] (http://www.silexsistemas.com.br)
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)


