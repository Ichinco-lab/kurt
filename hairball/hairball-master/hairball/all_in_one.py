import kurt
import os
import sys
import pdb
from plugins import HairballPlugin
from plugins import blocks
from hairball import Hairball


files = ['test/tmp.sb', 'file2', 'file3']
for file in files:
    args = ['-p', 'masteryNEU.Mastery', '-p', 'blocks.BlockCounts', file]
    hairball1 = Hairball(args)
    hairball1.initialize_plugins()
    hairball1.process()
    hairball1.finalize()
# scratchFile = "test/tmp.sb"
# outFile = "testresult.csv"
# hairball1.BlockCounts()
# print PC.finalize()
# print PC.analyze(scratchFile)
