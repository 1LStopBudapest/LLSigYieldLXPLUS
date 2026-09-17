Log in to lxplus account. Go to working directory.

Setup CMSSW area.
```
cmsrel CMSSW_14_1_0_pre4
cd CMSSW_14_1_0_pre4/src
cmsenv
```

Clone LLSigYieldLXPLUS directory.
```
git clone git@github.com:1LStopBudapest/LLSigYieldLXPLUS.git
```
Check LLSigCountDCHist.py that produces expected signal yield. Check the year and file list, sample list config (FileList_LLStops2018.py, SampleList.py). Now run LLSigCountDCHist.py locally.
```
python3 LLSigCountDCHist.py --nevents 2000
```
To submit condor jobs
```
cd ../../../
tar -zcvf CMSSW_14_1_0_pre4.tar.gz CMSSW_14_1_0_pre4
mv CMSSW_14_1_0_pre4.tar.gz CMSSW_14_1_0_pre4/src/LLSigYieldLXPLUS/condor
cd CMSSW_14_1_0_pre4/src/LLSigYieldLXPLUS/condor/
```
Activate grid certificate
```
voms-proxy-init --voms cms --valid 168:00
```
Copy the certificate executable from tmp to account home directory and link that path to condorScript.py. Change output file transfer path inside condorScript.py.

Now run following
```
python3 condorScript.py
```

Now to rename the output root file, the script, condor/Rename_condorfile.py can be used. 
