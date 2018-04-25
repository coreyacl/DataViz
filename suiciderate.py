import pandas as pd
import matplotlib as plt
import numpy as np


"""
Occupations:
    Plumber -       4
    Surgeon -       11
    Accountant -    13
    Software Eng -  15
    Mech E -        17
    Farmer -        22
    Physicist -     29

Data Type:
    Number -    0
    Percent -   1
"""
data = pd.read_csv("files/suiciderate.csv")
df = pd.DataFrame(data)


def get_profession_data(dataframe, profession, datatype):
    """ Takes the profession you want (in numerical form from the list above)
    and the datatype (either the total number or total percent) and returns
    that value
    """
    df2 = pd.DataFrame(dataframe['Total'].values.tolist()) #returns only totals
    profession = df2.iloc[profession] #gets row of desired profession
    profession_list = list(profession)
    profession_flist = profession_list[0].split() #splits data (percent and number are together in a cell)
    return profession_flist[datatype]

print(get_profession_data(df, 4,1))
