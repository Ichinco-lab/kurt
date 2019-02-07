import sys
#sys.path.append('/Users/michelle_ichinco/Documents/Research/kurt/tests')

import kurt
#print sys.path
import KurtToCSV
scratchFile = "tests/testFile1.sb2"
outFile = "testFile1.csv"

converter = KurtToCSV.KurtToCSV()
converter.KurtToCSVconvert(outFile,scratchFile)
