import os, sys

sys.path.append('../')
from SampleList import *

def get_parser():
    ''' Argument parser.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--year',             action='store',                     type=str,            default='2018',                                             help="Which year?" )
    argParser.add_argument('--region',             action='store',                    type=str,            default='SR+CR',                                           help="Which region?" )
    argParser.add_argument('--prxy',             action='store',                     type=str,            default='x509up_u43881',                                help="grid proxy file" )
    argParser.add_argument('--prxyPath',         action='store',                     type=str,            default='/afs/cern.ch/user/k/kmandal/',                  help="grid proxy file" )
    
    return argParser

options = get_parser().parse_args()
reg = options.region
year = options.year
proxy = options.prxy
ppath = options.prxyPath

nevts = -1
BrFrac = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

cq =len(LLsignals[year])



print('year: ', year)
print('tot signal mass points: ', cq)
print('total no of jobs: ',cq)
print('number of output root files each job peoduce: ',len(BrFrac))

bashline = []
bashline.append("#!/bin/bash\n")
bashline.append("\n")
bashline.append("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
bashline.append("export X509_USER_PROXY=$1\n")
bashline.append("voms-proxy-info -all\n")
bashline.append("voms-proxy-info -all -file $1\n")
bashline.append("\n")
bashline.append("tar -zxvf CMSSW_14_1_0_pre4.tar.gz\n")
bashline.append("cd CMSSW_14_1_0_pre4/src/\n")
bashline.append("scram b ProjectRename\n")
bashline.append("eval `scramv1 runtime -sh`\n")
bashline.append("scram b\n")
bashline.append("\n")
bashline.append("job=$3\n")
bashline.append("\n")
bashline.append("cd LLSignalYield\n")
for br in BrFrac:
    bashline.append("python3 LLSigCountDCHist.py --sidx $job --BR %s --region %s --year %s --nevents %d\n"%(br, reg, year, nevts))
bashline.append("\n")
bashline.append("mv *.root ../../../")
bashline.append("\n")
bashline.append("cd ../../../")
fsh = open("LLSigYieldCondor.sh", "w")
fsh.write(''.join(bashline))
fsh.close()


outputf = ['LLSigCountDCHist_'+reg+'_'+br for br in BrFrac]
subline = []
subline.append('executable              = LLSigYieldCondor.sh\n')
subline.append('Universe                = vanilla\n')
subline.append('+JobFlavour             = "testmatch"\n')
subline.append('output                  = LLSigYieldCondor.$(ClusterId).$(ProcId).out\n')
subline.append('error                   = LLSigYieldCondor.$(ClusterId).$(ProcId).err\n')
subline.append('log                     = LLSigYieldCondor.$(ClusterId).$(ProcId).log\n')
subline.append('getenv                  = True\n')
subline.append('should_transfer_files   = YES\n')
subline.append('when_to_transfer_output = ON_EXIT\n')
subline.append('transfer_output_files   = %s\n' % ', '.join('%s_$(ProcId).root' % f for f in outputf))
subline.append('output_destination      = root://eosuser.cern.ch//eos/user/k/kmandal/LLSignalYield/\n')
subline.append('\n\n')
subline.append('Proxy_filename = %s\n'%proxy)
subline.append('Proxy_path = %s$(Proxy_filename)\n'%ppath)
subline.append('Transfer_Input_Files    = $(Proxy_path), LLSigYieldCondor.sh, CMSSW_14_1_0_pre4.tar.gz\n')
subline.append('arguments               = $(Proxy_path) $(ClusterId) $(ProcId)\n')
subline.append('queue %i\n'%cq)

fs = open("LLSigYieldCondor.sub", "w")
fs.write(''.join(subline))
fs.close()
os.system('condor_submit LLSigYieldCondor.sub')

