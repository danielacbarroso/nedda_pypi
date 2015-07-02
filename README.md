# Nedda
## Automatic TNM cancer staging library

**What is cancer?**

In layman terms, the truth is that the word *cancer* actually refers to a huge number
of different diseases. They have in common the fact that they are an abnormal 
reproduction of cells that have the capability to spread to other organs and parts 
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
early, it can grow and spread to the lynphatic system (local and distant) and to
other organs (metastatic disease). In this case, the treatment options are distinct,
and the chance of cure much more remote.

**How is cancer staged**?

There is an system called TNM to classify each kind cancer. It is maintained by the
international medical community, through an organization called UICC. For each type
of cancer there is a table that maps some values to a specific stage. Those values are
known as T - the size of the tumor, N - the affected regional nodes, and M - the presence
of metastatic disease. Some kinds of cancer can also use other values on the computation. For
instance, to compute the stage for prostate cancer, it is also necessary to use the values of
PSA an Gleason.

The physician must know those values and manually look up on the specific table to correctly 
classify the cancer.

**How Nedda can help you?**



[1] http://www.cancer.gov/about-cancer/what-is-cancer
[2] American Cancer Society: Cancer Facts and Figures 2015. Atlanta, Ga: American Cancer Society, 2015. 
[3] Cancer Staging Handbook. From the AJCC Cancer Staging Manual. p. vii

