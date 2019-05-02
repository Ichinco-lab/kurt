import formatScratchData
from tslearn.utils import to_time_series_dataset
from tslearn.datasets import UCR_UEA_datasets
from tslearn.clustering import TimeSeriesKMeans
import time;

data = formatScratchData.formatScratchData("projects/projects.csv", "project_blocks/project_blocks.csv", 4, True)

formatScratchData.writeTimeSeriesToFile("timeSeries",data)
data = formatScratchData.readTimeSeriesFromFile("timeSeries")
for i in range(len(data[0])):
	print str(data[0][i]) + ":" + str(data[1][i])
"""



print "Getting Time Series"
#timeSeriesDataset = to_time_series_dataset(data[1])






startTime = time.time()
print "Cluster Start Time: " + str(startTime)
numClusters = 3
km = TimeSeriesKMeans(n_clusters=numClusters, metric="dtw", max_iter=3)
try:
	clusters = km.fit_predict(data[1])
except:
	print
endTime = time.time()
print "Cluster End Time: " + str(endTime)
print "Total Time: " + sr(endTime - startTime)
#print clusters

"""



def writeClustersToFile(filename,clusters):
	clusterFile = open(filename, "w")
	for cluster in clusters:
		clusterFile.write(str(cluster) + "\n")
	clusterFile.close()


def readClusterFromFile(filename):
	clusterFile = open(filename, "r")
	clusters = []
	for line in clusterFile:
		clusters.append(int(line))
	clusterFile.close()
	return clusters
