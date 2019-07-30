#import fileHandler
from FileHandler import fileHandler

"""
@param: tsData_
    The cluster time series dataset data file path for the first cluster
@param: centroidNumber
    The number/designation used to identify the specific
    cluster. Used for labeling purposes
@param: zoom
    Plots projects in range [0,zoom)
"""
def getAverageScores(tsData_,centroidNumber,zoom):#,tsKey_):
    tsData =  fileHandler.loadTSData(tsData_)

    avgArray = [[],[],[],[],[],[],[]]
    projCount = []
    for projectList in tsData:
        for proj in range(len(projectList[0:zoom])):
            try:
                projCount[proj] += 1.0
            except:
                projCount.append(1.0)
                for field in range(len(projectList[0:zoom][proj])):
                    avgArray[field].append(0.0)
            for field in  range(len(projectList[proj])):
                avgArray[field][proj] += float(projectList[0:zoom][proj][field])

    for proj in range(len(projCount)):
        for field in range(len(avgArray)):
            avgArray[field][proj] /=  projCount[proj]


    stdDev = [[],[],[],[],[],[],[]]
    for length in range(len(projCount)):
        for field in range(len(stdDev)):
            stdDev[field].append(0.0)

    for proj in range(len(projectList[0:zoom])):
        for field in range(len(projectList[proj])):
            stdDev[field][proj] += ((float(projectList[0:zoom][proj][field]) - avgArray[field][proj]) ** 2)

    for proj in range(len(projCount)):
        for field in range(len(stdDev)):
            stdDev[field][proj] =  ((stdDev[field][proj]/projCount[proj]) ** 0.5)

    labels = ["Synchronisation","Data Representation","Logical Thinking","Abstraction","User Interactivity","Parallelism","Flow Control"]
    colors = ['C0','C1','C2','C3','C4','C5','C6']
    plotAverageScores(avgArray,projCount,labels,centroidNumber,colors)
    for i in range(len(labels)):
        plotAverageScore(avgArray,stdDev,projCount,labels,centroidNumber,i,colors)

"""
@param: tsData_
    The cluster time series dataset data file path for the first cluster
@param: tsData1_
    The cluster time series dataset data file path for the second cluster
@param: zoom
    Plots projects in range [0,zoom)
"""
def plotAvgScoreComparison(tsData_,tsData1_,zoom):
    tsData =  fileHandler.loadTSData(tsData_)

    avgArray = [[],[],[],[],[],[],[]]
    projCount = []
    for projectList in tsData:
        for proj in range(len(projectList[0:zoom])):
            try:
                projCount[proj] += 1.0
            except:
                projCount.append(1.0)
                for field in range(len(projectList[0:zoom][proj])):
                    avgArray[field].append(0.0)
            for field in  range(len(projectList[proj])):
                avgArray[field][proj] += float(projectList[0:zoom][proj][field])

    for proj in range(len(projCount)):
        for field in range(len(avgArray)):
            avgArray[field][proj] /=  projCount[proj]

    labels = ["Synchronisation","Data Representation","Logical Thinking","Abstraction","User Interactivity","Parallelism","Flow Control"]
    colors = ['C0','C1','C2','C3','C4','C5','C6']

    tsData1 =  fileHandler.loadTSData(tsData1_)

    avgArray1 = [[],[],[],[],[],[],[]]
    projCount1 = []
    for projectList in tsData1:
        for proj in range(len(projectList[0:zoom])):
            try:
                projCount1[proj] += 1.0
            except:
                projCount1.append(1.0)
                for field in range(len(projectList[0:zoom][proj])):
                    avgArray1[field].append(0.0)
            for field in  range(len(projectList[proj])):
                avgArray1[field][proj] += float(projectList[0:zoom][proj][field])

    for proj in range(len(projCount1)):
        for field in range(len(avgArray1)):
            avgArray1[field][proj] /=  projCount1[proj]
    #for i in range(len(labels)):
    #
    #    plotAverageScore(avgArray,stdDev,projCount,labels,centroid,i,colors)
    for i in range(len(labels)):
        plotAverageScore(avgArray,avgArray1,projCount,labels,0,i,colors)

"""
@param: tsData_
    The cluster time series dataset data file path for the first cluster
@param: tsData1_
    The cluster time series dataset data file path for the second cluster
@param: zoom
    Plots projects in range [0,zoom)
"""
def plotAvgScoreDifference(tsData_,tsData1_,zoom):
        tsData =  fileHandler.loadTSData(tsData_)

        avgArray = [[],[],[],[],[],[],[]]
        projCount = []
        for projectList in tsData:
            for proj in range(len(projectList[0:zoom])):
                try:
                    projCount[proj] += 1.0
                except:
                    projCount.append(1.0)
                    for field in range(len(projectList[0:zoom][proj])):
                        avgArray[field].append(0.0)
                for field in  range(len(projectList[proj])):
                    avgArray[field][proj] += float(projectList[0:zoom][proj][field])

        for proj in range(len(projCount)):
            for field in range(len(avgArray)):
                avgArray[field][proj] /=  projCount[proj]

        labels = ["Synchronisation","Data Representation","Logical Thinking","Abstraction","User Interactivity","Parallelism","Flow Control"]
        colors = ['C0','C1','C2','C3','C4','C5','C6']

        tsData1 =  fileHandler.loadTSData(tsData1_)

        avgArray1 = [[],[],[],[],[],[],[]]
        projCount1 = []
        for projectList in tsData1:
            for proj in range(len(projectList[0:zoom])):
                try:
                    projCount1[proj] += 1.0
                except:
                    projCount1.append(1.0)
                    for field in range(len(projectList[0:zoom][proj])):
                        avgArray1[field].append(0.0)
                for field in  range(len(projectList[proj])):
                    avgArray1[field][proj] += float(projectList[0:zoom][proj][field])

        for proj in range(len(projCount1)):
            for field in range(len(avgArray1)):
                avgArray1[field][proj] /=  projCount1[proj]

        for proj in range(len(projCount)):
            for field in range(len(avgArray1)):
                avgArray1[field][proj] -= avgArray[field][proj]
                if avgArray1[field][proj] < 0:
                    avgArray1[field][proj] *= -1

        plotAverageScores(avgArray1,projCount,labels,"",colors)
        for i in range(len(labels)):
            plotAverageScoreDifference(avgArray1,projCount,labels,0,i,colors)



"""
@param: scores
    An array with the average scores for the first n projects by project
@param: projCount
    An array of the number of projects which are a users nth project
@param: labels
    The names of all dr. scratch fields in the order used in the timeseries
    dataset
@param: centroidNumber
    The label you use to identify the cluster. Used for labeling the graph
@param: colors
    An array with matplotlib color  codesof length equal to that of the labels
    array
"""
def plotAverageScores(scores,projCount,labels,centroidNumber,colors):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    x = np.linspace(0, 2, 100)
    for i in range(len(scores)):
        plt.plot(range(len(projCount)),scores[i],label=labels[i],color=colors[i])
        plt.axis([1,len(projCount),0,2])

    plt.xlabel('Progression')
    plt.ylabel('Complexity')
    plt.title("Cluster " +str(centroidNumber)+ " Average Scores")
    #plt.title("Full Dataset Average Scores")
    #plt.title("Average Score Difference")

    plt.legend()
    plt.tight_layout()
    plt.show()
	#print( matplotlib.rcParams['backend'])
    plt.savefig("Cluster" +str(centroidNumber)+ "AvgScores.png")
    #plt.savefig("FullDatasetAvgScores.png")
    #plt.savefig("AvgScoresDifference.png")
    import imp
    imp.reload(plt)


"""
@param: scores
    An array with the average scores for the first n projects by project
@param: projCount
    An array of the number of projects which are a users nth project
@param: labels
    The names of all dr. scratch fields in the order used in the timeseries
    dataset
@param: centroidNumber
    The label you use to identify the cluster. Used for labeling the graph
@param: scoreIndex
    The index of the field you want plotted
@param: colors
    An array with matplotlib color  codesof length equal to that of the labels
    array
"""
def plotAverageScoreDifference(scores,projCount,labels,centroidNumber,scoreIndex,colors):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    #print (len(projCount))
    x = np.linspace(0, 2, 100)
    #for i in range(len(scores)):
    plt.plot(range(len(projCount)),scores[scoreIndex],label=labels[scoreIndex],color=colors[scoreIndex])

    plt.axis([1,len(projCount),0,3])

    plt.xlabel('Progression')
    plt.ylabel('Difference in Complexity')
    plt.title("Average Score Difference: " + labels[scoreIndex])
    #plt.title("Full Dataset Average Scores: " + labels[scoreIndex])
    #plt.title("Cluster Comparison Average Scores: " + labels[scoreIndex])
    plt.legend()
    plt.tight_layout()
    plt.show()
    #print( matplotlib.rcParams['backend'])
    plt.savefig("AvgScoresDifference: " +labels[scoreIndex]+".png")
    #plt.savefig("FullDatasetAvgScores: " +labels[scoreIndex]+".png")
    #plt.savefig("ClusterComparisonAvgScores: " +labels[scoreIndex]+".png")
    import imp
    imp.reload(plt)

"""
@param: scores
    An array with the average scores for the first n projects by project
@param: stdDev
    An array with the standard deviation of scores
@param: projCount
    An array of the number of projects which are a users nth project
@param: labels
    The names of all dr. scratch fields in the order used in the timeseries
    dataset
@param: centroidNumber
    The label you use to identify the cluster. Used for labeling the graph
@param: scoreIndex
    The index of the field you want plotted
@param: colors
    An array with matplotlib color  codesof length equal to that of the labels
    array
"""
def plotAverageScore(scores,stdDev,projCount,labels,centroidNumber,scoreIndex,colors):
        import numpy as np
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        #print (len(projCount))
        x = np.linspace(0, 2, 100)
        #for i in range(len(scores)):
        plt.plot(range(len(projCount)),scores[scoreIndex],label=labels[scoreIndex],color=colors[scoreIndex])
        plt.plot(range(len(projCount)),stdDev[scoreIndex],label="Standard Deviation",color='C9')

        #plt.plot(range(len(projCount)),scores[scoreIndex],label="Cluster 0: " + labels[scoreIndex],color=colors[scoreIndex])
        #plt.plot(range(len(projCount)),stdDev[scoreIndex],label="Cluster 1: " + labels[scoreIndex],color='C9')


        plt.axis([1,len(projCount),0,2])

        plt.xlabel('Progression')
        plt.ylabel('Complexity')
        plt.title("Cluster " +str(centroidNumber)+ " Average Scores: " + labels[scoreIndex])
        #plt.title("Full Dataset Average Scores: " + labels[scoreIndex])
        #plt.title("Cluster Comparison Average Scores: " + labels[scoreIndex])
        plt.legend()
        plt.tight_layout()
        plt.show()
    	#print( matplotlib.rcParams['backend'])
        plt.savefig("Cluster" +str(centroidNumber)+ "AvgScores: " +labels[scoreIndex]+".png")
        #plt.savefig("FullDatasetAvgScores: " +labels[scoreIndex]+".png")
        #plt.savefig("ClusterComparisonAvgScores: " +labels[scoreIndex]+".png")
        import imp
        imp.reload(plt)
"""
@param: centroidFile
    The file which holds the cluster Centroids
@param: labels
    The names of all dr. scratch fields in the order used in the timeseries
    dataset
@param: centroidNumber
    Since the centroidFile holds all centroids this is needed to pick a
    specific one.
@param: colors
    An array with matplotlib color  codesof length equal to that of the labels
    array
Plots and saves the centroidNumber centroid onto a graph
"""
def plotCentroidScores(centroidFile,labels,centroidNumber,colors):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    centroid = fileHandler.loadClusterCenters(centroidFile)[centroidNumber]
    scores = [[],[],[],[],[],[],[]]
    for i in range(len(labels)):

        for project in range(len(centroid)):
            scores[i].append(centroid[project][i])
    print(centroid)
    for score in range(len(scores)):
        plt.plot(range(len(scores[score])),scores[score],label=labels[score],color=colors[score])



    plt.xlabel('Progression')
    plt.ylabel('Score')
    plt.title("Cluster " +str(centroidNumber)+ " Centroid")
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig("Cluster" +str(centroidNumber)+ "Centroid.png")
    import imp
    imp.reload(plt)

"""
@param: tsData_
    The path to the time series data.txt file to
    make a histogram from
@param: centroidNumber
    The number/designation used to identify the specific
    cluster. Used for labeling purposes
Creates a histogram of users who have coded different amounts
of projects total. Buckets start from [0,200) and are of size 200
"""
def getHistogram(tsData_,centroidNumber):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    #x = np.linspace(0, 2, 100)

    tsData = fileHandler.loadTSData(tsData_)
    #print(len(tsData))
    buckets = []
    c = []
    projCount = 0
    for projectList in tsData:
        try:
            buckets[int(len(projectList)/5)] += 1
        except:
            while len(buckets) < int(len(projectList)/5) + 1:
                buckets.append(0)
                c.append((len(buckets)-1) * 5)
            buckets[int(len(projectList)/5)] += 1
        projCount += 1
    print (str(centroidNumber) +":" +str(len(tsData)))
    #print (projCount)
    print (buckets[0:20])


    plt.hist(c,len(c),weights=buckets)
    plt.axis([0,200,0,15000])
    plt.xlabel('Number of Projects Created by the User')
    plt.ylabel('Number of Users')
    plt.title("Cluster " +str(centroidNumber)+ " Histogram")
    #plt.title("Full Dataset Histogram")
    #plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig("Cluster" +str(centroidNumber)+ "Histogram.png")
    #plt.savefig("FullDatasetHistogram.png")
    import imp
    imp.reload(plt)

"""
@param: tsKeys_
    an array with the names of cluster time series files (either a data.txt or a key.txt file by default)
Graphs and Saves a pie chart with each slice using the length of each loaded
file's array
"""
def getPieChart(tsKeys_):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    #tsData = fileHandler.loadTSData(tsData_)
    pie = []
    label = []
    for key in range(len(tsKeys_)):
        keySize = len(fileHandler.loadTSKey(tsKeys_[key]))
        pie.append(keySize)
        label.append("Cluster " + str(key))
    plt.pie(pie,labels=label,autopct='%1.1f%%',shadow=False,startangle=90,colors=["C1","C9"])
    #plt.axis('equal')
    plt.title("Cluster Distributions")
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig("ClusterDistributions.png")
    import imp
    imp.reload(plt)
#getAverageScores("Dataset/Centroid0/data.txt",0,150)
#getAverageScores("Dataset/Centroid1/data.txt",1,150)
#getAverageScores("Dataset/TSmain/data.txt",1,150)
#getAverageScores("Dataset/Test/Centroid0/data.txt",0,150)
#getAverageScores("Dataset/Test/Centroid1/data.txt",1,150)
#plotAvgScoreComparison("Dataset/Test/Centroid0/data.txt","Dataset/Test/Centroid1/data.txt",150)
#plotAvgScoreDifference("Dataset/Centroid0/data.txt","Dataset/Centroid1/data.txt",150)

getHistogram("Dataset/Test/Centroid0/data.txt",0)
getHistogram("Dataset/Test/Centroid1/data.txt",1)
#getHistogram("Dataset/TSMain/data.txt",0)

#plotCentroidScores("Dataset/Cluster/clusterCenters.txt", ["Synchronisation", "Data Representation", "Logical Thinking", "Abstraction", "User Interactivity", "Parallelism", "Flow Control"], 0, ['C0','C1','C2','C3','C4','C5','C6'])
#plotCentroidScores("Dataset/Cluster/clusterCenters.txt", ["Synchronisation", "Data Representation", "Logical Thinking", "Abstraction", "User Interactivity", "Parallelism", "Flow Control"], 1, ['C0','C1','C2','C3','C4','C5','C6'])

#getPieChart(["Dataset/Centroid0/data.txt","Dataset/Centroid1/data.txt"])
#getPieChart(["Dataset/Test/Centroid0/data.txt","Dataset/Test/Centroid1/data.txt"])
