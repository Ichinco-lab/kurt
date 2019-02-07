import array as arr
import sys
sys.path.append('/home/aaron/Programs/python/kurt/kurt')

#import kurt
#print sys.path
from KurtToCSV import KurtToCSV
scratchFiles = {"GlobalWarning2.sb2", "JackOSpook.sb2", "JustONEMoreHour.sb2", "SkippingRope.sb2", "TheMouseyMystery.sb2"}
outFile = "testFile1.csv"
mode = 'w'
converter = KurtToCSV()
#converter.KurtToCSVconvert(outFile,scratchFiles[0],'w')
for inFile in scratchFiles:
	converter.KurtToCSVconvert(outFile,inFile,mode)
	if mode == 'w':
		mode = 'a'
#converter.KurtToCSVconvert(outFile,"GlobalWarning2.sb2",'w')
"""converter.KurtToCSVconvert(outFile,"JackOSpook.sb2",'a')
converter.KurtToCSVconvert(outFile,"JustONEMoreHour.sb2",'a')
converter.KurtToCSVconvert(outFile,"SkippingRope.sb2",'a')
converter.KurtToCSVconvert(outFile,"TheMouseyMystery.sb2",'a')"""
