import sys
sys.path.append('/home/aaron/Programs/python/kurt/kurt')

#import kurt
#print sys.path
from KurtToCSV import KurtToCSV
scratchFile = "testFile1.sb2"
outFile = "testFile1.csv"

converter = KurtToCSV()
converter.KurtToCSVconvert(outFile,scratchFile)
