#!/usr/bin/python

import sys,os
import json
from ROOT import *

if __name__ == "__main__":

    tname = "sf/t"
    chain = TChain(tname)

    pattern = "ev*Elec*"
    chain.Add(pattern)

    #print "Entries found in chain:", chain.GetEntries()

    #cuts = "HT > 500 && LT > 250 && nLep == 1 && nEl == 1 && nVeto == 0 && Selected == 1 && nJets30Clean >=6 && nBJets30 > 0 && passFilters"
    cuts = "HT > 500 && LT > 250 && nLep == 1 && nEl == 1 && nVeto == 0 && Selected == 1 && nJets30Clean >=4 && nBJets30 > 0 && passFilters"
    #cuts = "HT > 500 && LT > 250 && nLep == 1 && nEl == 1 && nVeto == 0 && Selected == 1 && nJets30Clean >=4 && nJets30Clean <= 5 && nBJets30 > 0 && passFilters"
    #cuts += "&& abs(isSR) == 0"

    #var = "Run:Lumi:Event"

    # Get event list with selection
    chain.Draw('>>elist',cuts)
    elist = gDirectory.Get('elist')

    #format = "%i\t%i\t%i"
    format = "%i:%i:%i"
    #format = "Event == %i && Lumi == %i && Event == %i"

    for ev in xrange(elist.GetN()):
        tev = elist.GetEntry(ev)
        chain.GetEntry(tev)
        #if not mytree.isData:
        print format %(chain.Run, chain.Lumi, chain.Event)
