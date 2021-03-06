from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
import joblib
import numpy as np
model = joblib.load("model_full_June2020.jl")

depts = ['aafc-aac',
 'aandc-aadnc',
 'acoa-apeca',
 'aecl-eacl',
 'apfc-fapc',
 'atssc-scdata',
 'bdc',
 'cannor',
 'catsa-acsta',
 'cbsa-asfc',
 'cca-cac',
 'ccc',
 'ccohs-cchst',
 'cdev',
 'cdic-sadc',
 'ced-dec',
 'cer-rec',
 'cfia-acia',
 'cgc-ccg',
 'chrc-ccdp',
 'cib-bic',
 'cic',
 'cihr-irsc',
 'cmhc-schl',
 'cnlopb',
 'cnsc-ccsn',
 'cpc-cpp',
 'cpc-scp',
 'cra-arc',
 'crtc',
 'csa-asc',
 'csc-scc',
 'csec-cstc',
 'csis-scrs',
 'csps-efpc',
 'cstm-mstc',
 'cta-otc',
 'dcc-cdc',
 'dfatd-maecd',
 'dfo-mpo',
 'dnd-mdn',
 'ec',
 'edc',
 'elections',
 'erc-cee',
 'esdc-edsc',
 'fbcl-spfl',
 'fcac-acfc',
 'feddevontario',
 'fin',
 'fintrac-canafe',
 'fntc-cfpn',
 'fpcc-cpac',
 'glpa-apgl',
 'hc-sc',
 'iaac-aeic',
 'ic',
 'infc',
 'innovation',
 'irb-cisr',
 'isc-sac',
 'jccbi-pjcci',
 'jus',
 'lac-bac',
 'mgerc-ceegm',
 'mint-monnaie',
 'mpcc-cppm',
 'ncc-ccn',
 'nfb-onf',
 'ngc-mbac',
 'nnpa-apn',
 'nrcan-rncan',
 'nrc-cnrc',
 'nserc-crsng',
 'oag-bvg',
 'oci-bec',
 'ocl-cal',
 'ocol-clo',
 'oic-ci',
 'opc-cpvp',
 'osfi-bsif',
 'ovo-bov',
 'pbc-clcc',
 'pc',
 'pch',
 'pco-bcp',
 'phac-aspc',
 'pmprb-cepmb',
 'ppsc-sppc',
 'psc-cfp',
 'pshcp-rssfp',
 'psic-ispc',
 'pspib-oirpsp',
 'ps-sp',
 'pwgsc-tpsgc',
 'rcmp-grc',
 'sdtc-tddc',
 'ssc-spc',
 'sshrc-crsh',
 'statcan',
 'swc-cfc',
 'tbs-sct',
 'tc',
 'tf',
 'tpa-apt',
 'tsb-bst',
 'vac-acc',
 'vfpa-apvf',
 'viarail',
 'vrab-tacra',
 'wage',
 'wd-deo',
 'yesab-oeesy']

def predict_dept_prob(text):
    pct = np.round(model.predict_proba([text])[0],2)
    d = dict(zip(depts,pct))
    new={}
    for x in d.keys():
        if d[x] > 0:
            new[x]=d[x]
    return new