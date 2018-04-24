import numpy as np
import csv
import argparse

##Various Methods I found on parsing through csv files##
#https://stackoverflow.com/questions/35871920/numpy-loadtxt-valueerror-wrong-number-of-columns
#https://datascience.stackexchange.com/questions/14021/importing-csv-data-in-python/14022
#https://www.e-education.psu.edu/geog485/node/141
#https://docs.python.org/3/library/csv.html

#constructing an argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--csv", required=True,
    help="path to the input")

args = vars(ap.parse_args())

##Method 1##
#csvfile = np.genfromtxt("files/tabula-timework.csv", delimiter='\t',dtype='str')
#print(csvfile[5], csvfile[6])


##Method 2##
with open(args["csv"], newline='') as csvfile:
    timereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #header= csvReader.next()
    for row in timereader:
        print(', '.join(row))
