import pandas as pd
import matplotlib as plt
import numpy as np
import us_state_abbrev

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


The way to use this (in another script) is:

output = datacollection.get_specfic_value(database, profession, datatype)

for the average:

average = datacollection.get_average(database, datatype)
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
    colindex = database.columns.get_loc(column)
    #finding row index
    row, row_index = get_right_row(database, profession)
    #getting ouput
    output = database.iloc[int(row_index),int(colindex)]

    return output

def get_time_row(database, profession):
  """ like get riht rows except it stores multiple rows"""
  #converting to lowercase
  database.columns = database.columns.str.lower()
  database = database.apply(lambda x: x.astype(str).str.lower())
 # database['Occupation'] = database['Occupation'].str.lower()
  profession = profession.lower()
  #locating
  row_index = database.index[database['occupation'].str.contains(profession)].tolist()
  rows = []
  for i in row_index:
      rows.append(database.loc[i])
  return  rows

def get_hoursworked(profession, threshold):
    """
    This code will take a profession that you give it and find the accompanying
    row. Then it will parse that row to see which values are higher than the
    threshold. Next, it will create a list of those values and return the
    length of that list.

    ex: get_hoursworked('engineer', 40) #I want the hours that more than 40%
    of engineers are at work
    """
    time_data = []
    rows = get_time_row(timework_df, profession)
    all_time_data= []
    for i in rows:
        all_time_data.append(list(map(float, i[1:]))) #converts all of list to int

    #making one flat list
    flat_list = []
    for i in all_time_data:
        for j in i:
            flat_list.append(j)
    for i in flat_list:
        if i >= threshold:
            time_data.append(i)

    return len(time_data)

print(get_hoursworked('software', 1.0))

def get_average(database,  datatype):
    """This works for divorce rate and suicide rate. It takes all the rates or
    numbers and returns an average"""
    datatype = datatype.lower()
    database.columns = database.columns.str.lower()
    database = database.apply(lambda x: x.astype(str).str.lower())
    colNames = database.columns[database.columns.str.contains(pat = str(datatype))]
    column = colNames[0]
    average_data = database[column].tolist()
    #cleaning data
    np.nan_to_num(average_data)
    try:
        for i in average_data:
            if i == 'nan':
                average_data.remove(i)

    except:
        average_data.remove(i)
    #converting to float and taking mean
    average_data = np.array(average_data).astype(np.float)
    average = np.mean(average_data)

    return int(average)

###This is a helper function###
def convert_state_string(state):
    """This function takes the string of a state name in a state excel sheet and converts
        it to the state initial
    state = ''.join(filter(str.isalpha or str.isspace, state))
    initial = us_state_abbrev.us_state_abbrev.get(state)
    return initial
    """
    only_text = []
    for i in state:
        if i.isalpha() or i.isspace():
            only_text.append(i)
    result = ''.join(only_text)
    initial = us_state_abbrev.us_state_abbrev.get(result)
    return initial

###This is also a helper function###
def convert_list_state(state_list):
    """This function takes a list of states and converts them to their initials"""
    initial_list = []
    for item in state_list:
        initial = convert_state_string(item)
        initial_list.append(initial)
    return initial_list


def get_state_data(profession):
    """
    For this file, you have to enter the profession in the form:
    farm
    mech_eng
    physicist
    software
    surgeon

    for example: get_state_data('mech_eng')

    This function takes in one of the above strings and outputs a list of
    states in a uniform order, a list of corresponding number of employees,
    and the max value of employees.

    """
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    state = pd.read_excel("files/state_data/"+profession+".xlsx")
    state_df = pd.DataFrame(state)

    state_list = state_df['Area Name'].tolist()
    initial_list = convert_list_state(state_list)
    numbers_list = state_df['Employment'].tolist()

    #searching through and adding states and corresponding 0's
    initials = []
    for i in enumerate(states):
        if i[1] in states and i[1] not in initial_list:
            initials.append(i[1])
            try:
                numbers_list.insert(i[0], 0)
            except:
                numbers_list.append(0) #accounting for the less list indeces

    #completing the initials list
    for i in initial_list:
        initials.append(i)

    initials.sort(key=lambda x: states.index(x))

    #searching for highest value
    max_employment = max(numbers_list)

    return initials, numbers_list, max_employment
