from FileHandler import fileHandler
from math import floor as floor

"""
def func(tsData_,tsKey_):
    largest = 0
    key = 0
    tsData = fileHandler.loadTSData(tsData_)
    tsKey = fileHandler.loadTSData(tsKey_)
    for user in range(len(tsData)):
        for project in range(len(tsData[user][0])):
            if int(tsData[user][project][0]) > largest:
                largest = int(tsData[user][project][0])
                key = int(tsKey[user][project][0])
                print(str(largest) + ":" + str(key))
func("Dataset/TSMain/blockData.txt","Dataset/TSMain/project_iddata.txt")"""

def hist(tsBlockData_, tsData_,title, outFile, bucketSize):
    tsData = fileHandler.loadTSData(tsBlockData_)
    tsData1 = fileHandler.loadTSData(tsData_)
    buckets = [0]
    project_ids = []
    c = [0]
    for user in tsData:
        projects = 0
        for proj in range(len(user)):
            projects += int(user[proj][0])
        projects /= len(user)
        while len(buckets) < (int(floor(projects)) / bucketSize):
            buckets.append(0)
            project_ids.append([])
            c.append(len(c)*bucketSize)
        buckets.append(0)
        project_ids.append([])
        c.append(len(c)*bucketSize)
        buckets[int(int(floor(projects)) / int(bucketSize))] += 1
        project_ids[int(int(floor(projects)) / int(bucketSize))].append()

    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.hist(c,len(c),weights=buckets,label="Average Number of Blocks by Number of Users")
    #plt.axis([1,300,0,750])
    plt.axis([1,300,0,3500])
    plt.xlabel('Average Number of Blocks')
    plt.ylabel('Number of Users')
    plt.title(title+": Average Number of Blocks Histogram")
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig(outFile)
    import imp
    imp.reload(plt)


def getProjectBlockCountGraph(tsBlockData_,title,outFile):
    blockCounts = [0]
    projectCounts = [0]
    stdDev = [0]
    tsData = fileHandler.loadTSData(tsBlockData_)
    for user in tsData:
        for proj in range(len(user)):
            while len(user) > len(blockCounts):
                blockCounts.append(0)
                projectCounts.append(0)
                stdDev.append(0)
            projectCounts[proj] += 1
            blockCounts[proj] += int(user[proj][0])
    for proj in range(len(blockCounts)):
        blockCounts[proj] /= projectCounts[proj]



    for user in tsData:
        for proj in range(len(user)):
            stdDev[proj] += (int(user[proj][0]) - blockCounts[proj]) ** 2

    for proj in range(len(blockCounts)):
        if blockCounts[proj] != 0:
            stdDev[proj] /= blockCounts[proj]
            stdDev[proj] = stdDev[proj] ** 0.5




    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.plot(range(len(projectCounts)),blockCounts,label="Avg. Block Counts")
    plt.plot(range(len(projectCounts)),stdDev, label="Std. Deviation")
    #plt.axis([1,600,0,1600])
    #plt.axis([1,3000,0,3000])
    plt.xlabel('Progression')
    plt.ylabel('Average Block Count')
    plt.title(title+": Average Block Count")

    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.savefig(outFile)
    import imp
    imp.reload(plt)


#getProjectBlockCountGraph("Dataset/TSMain/blockData.txt","Full Dataset","FullDatasetAvgBlockCounts.png")
#getProjectBlockCountGraph("Dataset/Centroid0/blockData.txt","Cluster 0","Centroid0AvgBlockCounts.png")
#getProjectBlockCountGraph("Dataset/Centroid1/blockData.txt","Cluster 1","Centroid1AvgBlockCounts.png")
hist("Dataset/TSMain/blockData.txt", "Dataset/TSMain/project_idData.txt","Full Dataset", "FullDatasetHist.png", 5)
