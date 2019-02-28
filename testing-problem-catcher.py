import sys
#sys.path.append('/Users/michelle_ichinco/Documents/Research/kurt/tests')

import kurt
#print sys.path
from ProblemCatcher import ProblemCatcher
scratchFile = "tests/emptyControlTest.sb"#"tests/testsj2_empty_if.sb2"
#scratchFile ="tests/testsj2_empty_if.sb2"
outFile = "testFile1.csv"

PC = ProblemCatcher()
PC.emptyConditionHandler.test_emptyConditionHandler(scratchFile)
#print PC.hide_show_problem(scratchFile)
#print PC.multiple_if(scratchFile)
# print PC.if_noelse(scratchFile)
# print PC.if_nocode(scratchFile)
