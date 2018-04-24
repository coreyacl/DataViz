import pandas as pd
import matplotlib as plt
import numpy as np

data = pd.read_csv("files/tabula-timework.csv")
df = pd.DataFrame(data)

"""
Names to input into the function and the corresponding profession:
Mech E -        Architecture and engineering occupations................ .
Software Eng -  Computer and mathematical occupations................ .
Farmer -        Farming, fishing, and forestry occupations.................. .
Plumber -       Installation, maintenance, and repair occupations. . . . . . . . .
Accountant -    Business and financial operations occupations......... .
Physicist -     Life, physical, and social science occupations.......... .
Surgeon -       Healthcare practitioner and technical occupations. . . . . . 


def get_profession_data(dataframe, profession):
    """
    This code will take a string that exactly matches one in the file and returns
    all the values in the accompanying row."""
    output = []
    for row in dataframe.itertuples():
        if profession in row:
            dataframe2 = dataframe.xs(row[0]) #taking the right rows
            my_list = dataframe2.tolist() #converting to list
            my_list = my_list[1:] #getting rid of title
            output.extend(my_list) #put into final list
    return output

def get_hoursworked(dataframe, profession, threshold):
    """
    This code will take a profession that you give it and find the accompanying
    row. Then it will parse that row to see which values are higher than the
    threshold. Next, it will create a list of those values and return the
    length of that list.
    """
    time_data = []
    all_time_data = get_profession_data(dataframe, profession)
    all_time_data = list(map(float, all_time_data)) #converts all of list to int
    for i in all_time_data:
        if i >= threshold:
            time_data.append(i)

    return len(time_data), time_data


print(get_hoursworked(df, 'Life, physical, and social science occupations.......... .', 45.0))
