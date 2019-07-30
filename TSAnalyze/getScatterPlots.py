from FileHandler import fileHandler


def scatterPlotBlockProjectCounts(blockCountData_,saveToFile):
    #First load the block count data
    blockCountData = fileHandler.loadTSData(blockCountData_)

    avgBlockCounts = [] #Holds The average amount of blocks by user
    projectCounts  = [] #Holds The the number of projects by user


    for user in range(len(blockCountData)):
        #Initialize spots in lists to put data for current user
        avgBlockCounts.append(0.0)
        projectCounts.append(len(blockCountData[user]))
        #To get the average block count for each users
        #first add the block counts for all of a users projects together
        for proj in range(len(blockCountData[user])):
            avgBlockCounts[user] += float(blockCountData[user][proj][0])
            #then divide the sum by the total number of projects created by the user
        avgBlockCounts[user] /= float(projectCounts[user])

    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from scipy.stats import gaussian_kde
    ###################################################
    xy = np.vstack([projectCounts,avgBlockCounts])
    z = gaussian_kde(xy)(xy)
    #One or Both of these is too
    #slow. Need to add in s save function for after they run
    ###################################################
    plt.scatter(projectCounts,avgBlockCounts,c=z,s=1,edgecolor='')
    #plt.axis([0,3000,0,500])#2 (1 is using default for axis)
    #plt.axis([0,500,0,5000])#3
    #plt.axis([0,500,0,500])#4
    #plt.axis([0,100,0,100])#5
    plt.axis([0,100,0,200])#6
    #plt.axis([0,500,0,200])#7

    plt.xlabel('Number of Projects')
    plt.ylabel('Average Number of Blocks Per Project')
    plt.title("Average Number of Blocks Per Project Over Number of Projects")


    plt.savefig(saveToFile)
    import imp
    imp.reload(plt)



scatterPlotBlockProjectCounts("temp2/data.txt","temp2/out6.png")
