import sys
#sys.path.append('/Users/michelle_ichinco/Documents/Research/kurt/tests')

import kurt
#print sys.path
from ProblemCatcher import ProblemCatcher
scratchFile = "tests/testFile1.sb2"
outFile = "testFile1.csv"

PC = ProblemCatcher()
print (PC.hide_show_problem(scratchFile))
