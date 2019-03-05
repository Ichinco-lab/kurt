import kurt
import os
import sys
import pdb
from plugins import HairballPlugin
from plugins import blocks
from hairball import Hairball

#To take in multiple files
files = ['test/tmp.sb', 'test/testsj1.sb2', 'test/testsj2_empty_if.sb2']
#To iterate over all the files and analyze all the plugins on each one of them
for file in files:
    args = ['-p', 'masteryNEU.Mastery', '-p', 'blocks.BlockCounts', '-p', 'blocks.DeadCode', file]
    hairball1 = Hairball(args)
    hairball1.initialize_plugins()
    hairball1.process()
    hairball1.finalize()
# scratchFile = "test/tmp.sb"
# outFile = "testresult.csv"
# hairball1.BlockCounts()
# print PC.finalize()
# print PC.analyze(scratchFile)
