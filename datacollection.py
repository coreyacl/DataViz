import pandas as pd
import matplotlib as plt
import numpy as np

"""
OES_Report contains
  employment
  hourly mean wage
  annual mean wage
  hourly median wage
  annual median wage

Tabula-Timework contains
  hours worked
  times of day and percent of workers working at that time

suiciderate contains
  suicide rates by profession
  average rate

Tabula-divorce contains
  divorce rates by profession
  average rate

Tabula-gender contains
  gender ratio by profession
  average gender ratio

State Data contains
  list of states
  corresponding list of number of employees
  highest value in the list


The way to use this is:

output = datacollection.get_specfic_value(database, profession, datatype)
"""

#creating all the databases

OES = pd.read_excel("files/OES_Report(1).xlsx")
OES_df = pd.DataFrame(OES)

timework = pd.read_csv("files/tabula-timework.csv")
timework_df = pd.DataFrame(timework)

suiciderate = pd.read_csv("files/suiciderate.csv")
suiciderate_df = pd.DataFrame(suiciderate)

divorcerate  = pd.read_csv('files/tabula-divorce.csv')
divorcerate_df = pd.DataFrame(divorcerate)


def get_right_row(database, profession):
  #converting to lowercase
  database.columns = database.columns.str.lower()
  database = database.apply(lambda x: x.astype(str).str.lower())
 # database['Occupation'] = database['Occupation'].str.lower()
  profession = profession.lower()
  #locating
  row_index = database.index[database['occupation'].str.contains(profession)].tolist()
  row_index = row_index[0]
  df2 = database.loc[row_index]
  return  df2, row_index

def get_specfic_value(database, profession, datatype):
    """This works for OES data, divorce rate, suicide rate"""
    #formatting
    datatype = datatype.lower()
    database.columns = database.columns.str.lower()
    database = database.apply(lambda x: x.astype(str).str.lower())

    #finding the column and its index
    colNames = database.columns[database.columns.str.contains(pat = str(datatype))]
    column = colNames[0]
    colindex = OES_df.columns.get_loc(column)
    #finding row index
    row, row_index = get_right_row(database, profession)
    #getting ouput
    output = database.iloc[int(row_index),int(colindex)]

    return output

def get_hoursworked(dataframe, profession, threshold):
    """
    This code will take a profession that you give it and find the accompanying
    row. Then it will parse that row to see which values are higher than the
    threshold. Next, it will create a list of those values and return the
    length of that list.
    """
    time_data = []
    all_time_data, row_index = get_right_row(dataframe, profession)
    all_time_data = list(map(float, all_time_data[1:])) #converts all of list to int
    for i in all_time_data:
        if i >= threshold:
            time_data.append(i)

    return len(time_data)
