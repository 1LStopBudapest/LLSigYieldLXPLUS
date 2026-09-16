#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
export X509_USER_PROXY=$1
voms-proxy-info -all
voms-proxy-info -all -file $1

tar -zxvf CMSSW_14_1_0_pre4.tar.gz
cd CMSSW_14_1_0_pre4/src/
scram b ProjectRename
eval `scramv1 runtime -sh`
scram b

job=$3

cd LLSignalYield
python3 LLSigCountDCHist.py --sidx $job --BR 01 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 02 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 03 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 04 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 05 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 06 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 07 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 08 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 09 --region SR+CR --year 2018 --nevents -1
python3 LLSigCountDCHist.py --sidx $job --BR 10 --region SR+CR --year 2018 --nevents -1

mv *.root ../../../
cd ../../../