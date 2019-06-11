import csv


"""
@param: scores_
    The path to a csv file with 2 columns, numClusters, and score
@param: numInstances
    The number of times a given number of clusters appears. This program
    assumes that all num clusters should occur the same amount.
"""
def printAvgScores(scores_):
    scores = open(scores_, "r")#initialize the csv reader
    readScores = csv.DictReader(scores)
    AvgScores = {}
    count = {}
    for score in readScores:
        try:
            AvgScores[score['numClusters']] += float(score["score"])
            count[score['numClusters']] += 1
        except:
            AvgScores.update({score['numClusters']:float(score["score"])})
            count.update({score['numClusters']:1})
    for row in AvgScores.keys():
        print(str(row) + ": " + str((float(AvgScores[row]) / float(count[row]))))
    scores.close()


printAvgScores("TSDataset/sscores.csv")
