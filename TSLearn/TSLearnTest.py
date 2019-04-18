"""from tslearn.utils import to_time_series
my_first_time_series = [1, 8, 6, 6]
formatted_time_series = to_time_series(my_first_time_series)
print(formatted_time_series.shape)"""

from tslearn.utils import to_time_series_dataset
from tslearn.datasets import UCR_UEA_datasets
from tslearn.clustering import TimeSeriesKMeans

my_first_time_series  = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
my_second_time_series = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
my_third_time_series  = [[6,6],[6,6],[6,6],[6,6],[6,6],[6,6],[6,6]]
my_fourth_time_series = [[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8]]
d5 = my_first_time_series

#my_first_time_series  = [0,0,0,0,0,0,0]
#my_second_time_series = [1,1,1,1,1,1,1]
#my_third_time_series  = [6,6,6,6,6,6,6]
#my_fourth_time_series = [8,8,8,8,8,8,8]
formatted_dataset = to_time_series_dataset([my_first_time_series,
                                                my_second_time_series,
                                                my_third_time_series,
												my_fourth_time_series,
												d5])
formatted_dataset1 = to_time_series_dataset([my_fourth_time_series,
												my_third_time_series,
                                                my_second_time_series,
                                                my_first_time_series
						])
#formatted_dataset1 = to_time_series_dataset([my_fourth_time_series])
#print(formatted_dataset.shape)
#print(formatted_dataset)


from tslearn.utils import save_timeseries_txt, load_timeseries_txt
save_timeseries_txt("datasetExample.txt", formatted_dataset)


#x_train, y_train, x_test, y_test = UCR_UEA_datasets().load_dataset("datasetExample.txt")
#ucr_var = UCR_UEA_datasets().load_dataset("datasetExample.txt")
#print ucr_var
print "Output:"
km = TimeSeriesKMeans(n_clusters=3, metric="dtw", max_iter=200)#.fit(formatted_dataset)
clusters = km.fit_predict(formatted_dataset)
print clusters
#cl = clusters[0]
#for cluster in range(len(clusters)):
#	if clusters[cluster] ==  cl:
#		print formatted_dataset[cluster]
#	else:
#		print "formatted_dataset[" + str(cluster) + "] not part of the focus cluster"

import numpy
import matplotlib.pyplot as plt
#pip install matplotlib
#sudo dnf install pythion-tkinter
sz=13
for yi in range(3):
    plt.subplot(3, 3, 4 + yi)
    for xx in formatted_dataset[clusters == yi]:
        plt.plot(xx.ravel(), "k-", alpha=.2)
    plt.plot(km.cluster_centers_[yi].ravel(), "r-")
    plt.xlim(0, sz)
    plt.ylim(-4, 4)
    if yi == 1:
        plt.title("Test Graph")

plt.tight_layout()
plt.show()

