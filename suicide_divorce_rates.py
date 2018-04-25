import pandas as pd
import matplotlib as plt
import numpy as np


"""
Info for Suicide Rate Function:
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


def get_suicide_data(dataframe, profession, datatype):
    """ Takes the profession you want (in numerical form from the list above)
    and the datatype (either the total number or total percent) and returns
    that value
    """
    df2 = pd.DataFrame(dataframe['Total'].values.tolist()) #returns only totals
    profession = df2.iloc[profession] #gets row of desired profession
    profession_list = list(profession)
    profession_flist = profession_list[0].split() #splits data (percent and number are together in a cell)
    return profession_flist[datatype]



"""
Info for Divorce Rate Function:
Occupations:
    Farmer -        377
    Plumber -       277
    Surgeon -       389
    Accountant -    347
    Software E -    430
    Physicist -     447
    Mech E -        473
"""
df2  = pd.read_csv('files/tabula-divorce.csv')
df2 = pd.DataFrame(df2)

def get_divorce_data(database, occupation):
    """when given database and occupation (from above), returns rate of divorce.
    """
    return dataframe['Unnamed: 2'].values[occupation]
