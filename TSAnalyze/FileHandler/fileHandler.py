"""
Dependencies: six, csv
"""
import six; from six.moves import cPickle as pickle

"""The following functions wrap the functionality
of cpickle to save or load the timeseries and its key"""
def saveTSKey(filename, timeSeries):
	with open(filename, 'wb') as f:
   		pickle.dump(timeSeries[0], f)
def loadTSKey(filename):
	f = open(filename, 'rb')
	key = pickle.load(f)
	return key
def saveTSData(filename, timeSeries):
	with open(filename, 'wb') as f:
   		pickle.dump(timeSeries[1], f)
def loadTSData(filename):
	f = open(filename, 'rb')
	data = pickle.load(f)
	return data

"""
Saving and Loading The Actual Custers
"""
def saveClusters(filename,clusters):
	with open(filename, 'wb') as f:
		pickle.dump(clusters, f)
		f.close()

def loadClusters(filename):
	f = open(filename, 'rb')
	clusters = pickle.load(f)
	f.close()
	return clusters


"""
Saving and Loading The Cluster Centroids
"""
def saveClusterCenters(filename, clusterer):
	with open(filename, 'wb') as f:
		pickle.dump(clusterer.cluster_centers_, f)
		f.close()

def loadClusterCenters(filename):
	f = open(filename, 'rb')
	clusterCenters = pickle.load(f,encoding='latin1')
	f.close()
	return clusterCenters
