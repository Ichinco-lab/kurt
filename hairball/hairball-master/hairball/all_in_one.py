import kurt
import os
import sys
import pdb
from plugins import HairballPlugin
from plugins import blocks
from hairball import Hairball

# pdb.set_trace()
args = ['-p', 'masteryNEU.Mastery', 'blocks.BlockCounts', 'test/tmp.sb']
hairball1 = Hairball(args)
hairball1.initialize_plugins()
hairball1.process()
hairball1.finalize()
# scratchFile = "test/tmp.sb"
# outFile = "testresult.csv"
# hairball1.BlockCounts()
# print PC.finalize()
# print PC.analyze(scratchFile)
