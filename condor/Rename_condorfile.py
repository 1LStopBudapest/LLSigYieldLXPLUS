import os
import sys
import math
import ROOT
import re

sys.path.append('../')
from SampleList import *

year = "2018"
signals = LLsignals[year]
BrFrac = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

for i, suffix in enumerate(signals):
    for br in BrFrac:
        old_filename = "/eos/user/k/kmandal/LLSignalYield/LLSigCountDCHist_SR+CR_"+br+"_{}.root".format(i)
        new_filename = f"/eos/user/k/kmandal/LLSignalYield/LLSigCountDCHist_SR+CR_{br}_{suffix}.root"
            
        if os.path.exists(old_filename):
            os.rename(old_filename, new_filename) #Do one dry run (with commenting out this line) before actual renaming
            print(f"Renamed: {old_filename} -> {new_filename}")
        else:
            print(f"Warning: {old_filename} not found!")

