import fileHandler

def getFirstXofYthTS(tsData_,ythTS,firstX):
    tsData = fileHandler.loadTSData(tsData_)
    if ythTS in range(len(tsData)):
        if firstX in range(len(tsData[ythTS])):
            for i in range(firstX):
                print(tsData[ythTS][i])

            #print(tsData[ythTS][0:firstX])





#getFirstXofYthTS("Dataset/Centroid0/data.txt",0,7)
