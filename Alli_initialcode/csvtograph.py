"""
Importing files from a csv file and displaying them on a graph.
"""

#source : https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/


import matplotlib.pyplot as plt
import csv
import numpy as np

#creating a list of professions
lifescience = []
farmer = []
business = []
computer = []
repair = []
engineering = []
professions = [lifescience, farmer, business, computer, repair, engineering]
x_real= []
y = [] #for the y axis of the graph , later

def store_data_list(file_name, csv_text, profession_list):
    """
    Takes the file and finds the row with the text you're looking for. In this
    case, it will take the name of a profession and returns a list that contains
    the name of the profession and the data associated with it. In the example I'm using,
    it's time.
    """
    with open(file_name, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=",")
        for row in plots:
            if csv_text in row:
                profession_list.append(row)


store_data_list('files/tabula-timework.csv', 'Life, physical, and social science occupations.......... .',lifescience)
store_data_list('files/tabula-timework.csv', 'Farming, fishing, and forestry occupations.................. .',farmer)
store_data_list('files/tabula-timework.csv', 'Business and financial operations occupations......... .',business)
store_data_list('files/tabula-timework.csv', 'Computer and mathematical occupations................ .',computer)
store_data_list('files/tabula-timework.csv', 'Installation, maintenance, and repair occupations. . . . . . . . .',repair)
store_data_list('files/tabula-timework.csv', 'Architecture and engineering occupations................ .', engineering)

for profession in professions:
    #Creating x axis
    x_real.append(profession[0][0]) #adding name as x coordinate
    #Creating y axis
    morning = (profession[0][1:])
    afternoon = (profession[1][1:])
    times = morning+afternoon
    y.append(times)


x = np.arange(24)
print(y)

for i in y:
    plt.plot(x, i)

plt.legend(['Physical Science', 'Farming', 'Business', 'Comp Sci', 'Repair/ Plumbing', 'Engineering'])
plt.show()

"""
Problems that need to be solved:
-make it more generalized
-make it easier to search for data in csv files
"""
