import os, sys
import ROOT
import subprocess
import types

import FileList_LLStops2018
import FileList_LLStops2017
import FileList_LLStops2016PreVFP
import FileList_LLStops2016PostVFP


class SampleChain():
    #values /pb
    luminosity_2016PreVFP     = 19520.0
    luminosity_2016PostVFP     = 16810.0
    luminosity_2016           = 36330.0
    luminosity_2017           = 41856.0
    luminosity_2018           = 58905.0


    def __init__(self, sample, startfile, filestorun, year='2018', treename = "Events"):
        year_str = str(year)
        self.sample = sample
        self.startfile = startfile
        self.filestorun = filestorun
        self.treename = treename
        if year_str=='2016PreVFP':
            self.samplelist = FileList_LLStops2016PreVFP.samples
        elif year_str=='2016PostVFP':
            self.samplelist = FileList_LLStops2016PostVFP.samples
        elif year_str=='2016':
            self.samplelist = FileList_LLStops2016.samples
        elif year_str=='2017':
            self.samplelist = FileList_LLStops2017.samples 
        else:
            self.samplelist = FileList_LLStops2018.samples 
        self.gredir = 'root://eosuser.cern.ch/'        

    def getchains(self):
        ch03 = ROOT.TChain(self.treename)
        ch10 = ROOT.TChain(self.treename)
        filelist03 = []
        filelist10 = []
        filelist03.append(self.samplelist['stopLL'][0] + 'merged_'+ self.sample + '_BR_0.3_processed.root')
        self.addtochain(ch03, filelist03, 0, 1)
        filelist10.append(self.samplelist['stopLL'][0] + 'merged_'+ self.sample + '_BR_1.0_processed.root')
        self.addtochain(ch10, filelist10, 0, 1)
        return ch03, ch10

    @staticmethod
    def getfilelist(filedir):
        files = []
        ls = subprocess.Popen(["find", filedir, "-type", "f"], stdout=subprocess.PIPE)
        fs = ls.stdout
        for f in fs:
            files.append(f.strip("\n"))

        return files

    def addtochain(self, ch, filelist, startfile, filestorun):
        files = len(filelist)-startfile if filestorun == -1 else filestorun 
        for i in range(len(filelist)):
            if i < startfile or i > (startfile+files)-1: continue
            ch.Add(self.gredir+filelist[i])
            
    def getEntries(self, ch):
        return ch.GetEntries()

    def getSampleList(self):
        return self.samplelist
