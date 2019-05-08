import formatScratchData
import cPickle as pickle
from tslearn.utils import to_time_series_dataset
from tslearn.datasets import UCR_UEA_datasets
from tslearn.clustering import TimeSeriesKMeans
import time;

def writeClustersToFile(filename,clusters):
	with open(filename, 'wb') as f:
   		pickle.dump(clusters, f)
		f.close()


def readClusterFromFile(filename):
	f = open(filename, 'rb')
	clusters = pickle.load(f)
	f.close()
	return clusters

def saveClusterCenters(filename, clusterer):
	with open(filename, 'wb') as f:
   		pickle.dump(clusterer.cluster_centers_, f)
		f.close()

def loadClusterCenters(filename):
	f = open(filename, 'rb')
	clusterCenters = pickle.load(f)
	f.close()
	return clusterCenters

"""If time series dataset not made yet use this"""
#data = formatScratchData.formatScratchData("projects/projects.csv", "project_blocks/project_blocks.csv", 500, True)

#formatScratchData.saveTimeSeries("timeSeries.txt",data)
#formatScratchData.saveTimeSeriesKey("timeSeriesKey.txt",data)
"""end of this"""



data = formatScratchData.loadTimeSeries("timeSeries.txt")

print len(data)

print "Getting Time Series"
timeSeriesDataset = to_time_series_dataset(data)






startTime = time.time()
print "Cluster Start Time: " + str(startTime)
numClusters = 3
km = TimeSeriesKMeans(n_clusters=numClusters, metric="softdtw", max_iter=3)
try:
	clusters = km.fit_predict(timeSeriesDataset)
except:
	print "Cluster Failure"
endTime = time.time()
print "Cluster End Time: " + str(endTime)
print "Total Time: " + str((endTime - startTime)/3600) + "hours"
writeClustersToFile("clusters.txt", clusters)
clusters = readClusterFromFile("clusters.txt")

saveClusterCenters("clusterCenters.txt", km)
clusterCenters = loadClusterCenters("clusterCenters.txt")








import numpy
import matplotlib.pyplot as plt


sz=1
for yi in range(3):
    plt.subplot(3, 3, 4 + yi)
    for xx in timeSeriesDataset[clusters == yi]:
        plt.plot(xx.ravel(), "k-", alpha=.2)
    plt.plot(clusterCenters[yi].ravel(), "r-")
    plt.xlim(0, sz)
    plt.ylim(0, 4)
    if yi == 1:
        plt.title("Test Cluster Graph")

plt.tight_layout()
plt.show()







