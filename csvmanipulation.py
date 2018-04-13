import numpy as np


csvfile = np.genfromtxt("files/tabula-timework.csv", delimiter='\t',dtype='str')
print(csvfile[5], csvfile[6])

#https://stackoverflow.com/questions/35871920/numpy-loadtxt-valueerror-wrong-number-of-columns
#https://datascience.stackexchange.com/questions/14021/importing-csv-data-in-python/14022
#https://www.e-education.psu.edu/geog485/node/141
#https://docs.python.org/3/library/csv.html
