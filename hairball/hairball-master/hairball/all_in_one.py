import kurt
import os
import sys
from plugins import HairballPlugin
from plugins import blocks
from hairball import Hairball

hairball1 = Hairball(sys.argv[1:])
hairball1.initialize_plugins()
hairball1.process()
hairball1.finalize()
scratchFile = "test/tmp.sb"
outFile = "testresult.csv"
PC = blocks.BlockCounts()
print PC.finalize()
# print PC.analyze(scratchFile)
