import fileHandler
import os

"""
@param: clusterKey_
    The path to the cluster key file
@param: tsData_
    The path to the time series data file that the cluster was built from
@param: tsKey_
    The path to the time series key file that the cluster key corresponds too
@param: path
    The path to where you want to put the output files
@param: outFile
    The name of the file you want data stored to
"""
def split(clusterKey_, tsData_, tsKey_,path,outFile="/data.txt"):
    clusterKey = fileHandler.loadClusters(clusterKey_)
    centroids = {}
    tsData =  fileHandler.loadTSData(tsData_)
    tsKey = fileHandler.loadTSKey(tsKey_)
    for i in range(len(clusterKey)):
        try:
            centroids[str(clusterKey[i])][0].append(tsKey[i])
            centroids[str(clusterKey[i])][1].append(tsData[i])
        except:
            centroids.update({str(clusterKey[i]):[[tsKey[i]],[tsData[i]]]})


    for centroid in centroids.keys():
        filepath = path + "/Centroid" +str(centroid)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        fileHandler.saveTSKey(filepath + "/key.txt",centroids[centroid])
        fileHandler.saveTSData(filepath + "/"+ outFile,centroids[centroid])


def printClusterKey(tsKey_):
    tsKey = fileHandler.loadTSKey(tsKey_)
    for key in tsKey:
        print (key)



split("Dataset/Cluster/clusters.txt","Dataset/TSmain/data.txt","Dataset/TSmain/key.txt","Dataset/Test","data.txt")
#split("Dataset/Cluster/clusters.txt","Dataset/TSmain/blockData.txt","Dataset/TSmain/key.txt","Dataset","blockData.txt")
#printClusterKey("Dataset/Centroid0/key.txt")
#printFirstXProjectIds("Dataset/Centroid0/data.txt",7)
