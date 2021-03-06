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

race contains
    race ratio by profession
    average race ratio

Spending contains
    spending by profession type
    average spending

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

gender = pd.read_csv('files/tabula-gender.csv')
gender_df = pd.DataFrame(gender)

race = pd.read_excel("files/race.xlsx")
race_df = pd.DataFrame(race)

spending = pd.read_csv('files/spending.csv')
spending_df = pd.DataFrame(spending)

spending_df = df = spending_df.set_index('item').T.rename_axis('occupation').rename_axis(None, 1).reset_index()



### General Data Functions ###

def get_right_row(database, profession):
  """This is a helper function for get_specific_value. You don't need to use it.
  It finds the right row in a database"""
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
    """This works for OES data, divorce rate, suicide rate, gender ratio, spending
    *note : for divorce rate, the profession for mech e is "mechanical engineer"
            also for divorce rate, the profession for software is "software developer"
    *note 2: the same applies for race. Also, the physicist data doesn't exist. Also,
    the columns for the race data are : White, Black or African American,
    Asian, Hispanic or Latino

    """
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


### Time Functions ###

def get_time_row(database, profession):
  """ This is a helper function for get_hoursworked - You don't need to use it.
  It works like get right rows except it stores multiple rows"""
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

def get_hoursworked(profession):
    """
    This code will take a profession that you give it and find the accompanying
    row. It will return a list of all the hours of the day and the percentage of
    workers in the specified occupation working at that hour.

    ex: times, percentage = get_hoursworked('engineer') , times come first
    """
    time_data = []
    rows = get_time_row(timework_df, profession)
    all_time_data= []
    for i in rows:
        all_time_data.append(list(map(float, i[1:]))) #converts all of list to int

    #making one flat list

    for i in all_time_data:
        for j in i:
            time_data.append(j)

    #making list of hours
    list_times = list(timework_df.columns.values[1:]) #finding am values (they're the index)
    #Evening times are nested in as a row
    index_evening = timework_df.index[timework_df['occupation'].str.match('Occupation')].tolist()
    list_evening = timework_df.iloc[int(index_evening[0])].values[1:] #even though its one value, index_evening returns a list
    list_times.extend(list_evening)

    return  list_times,  time_data


### Average Function ###

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

###### State Functions #######

def convert_state_string(state):
    """ This is a helper function. You don't need to use it.
    This function takes the string of a state name in a state excel sheet and converts
        it to the state initial
    """
    only_text = []
    for i in state:
        if i.isalpha() or i.isspace():
            only_text.append(i)
    result = ''.join(only_text)
    initial = us_state_abbrev.us_state_abbrev.get(result)
    return initial


def convert_list_state(state_list):
    """ This is also a helper function. You don't need to use it.
    This function takes a list of states and converts them to their initials"""
    initial_list = []
    for item in state_list:
        initial = convert_state_string(item)
        initial_list.append(initial)
    return initial_list


def get_state_data(profession):
    """
    For this function, you have to enter the profession in the form:
    'farm'
    'mech_eng'
    'physicist'
    'software'
    'surgeon'

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

    #filtering out none
    for i in initial_list:
        if i == None:
            initial_list.remove(i)

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
