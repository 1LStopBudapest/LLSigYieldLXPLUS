import ROOT
import os, sys 
import pandas as pd


class GenFilterEff():
        def __init__(self):
                self.csvFile = "csv_appended_filterEff.csv"

        def getEff(self, mStop, mNeu):
                df = pd.read_csv(self.csvFile, usecols= ["m","dm","filterEff"])
                if mStop%5 != 0:
                        mStop = mStop-1 if  mStop%5 == 1 else mStop-2 #assuming max diff is 2 and only happens for mstop
                dM = mStop - mNeu
                filterEff = df.loc[(df.m==mStop ) & (df.dm==dM ),'filterEff'].values[0]
                return filterEff

