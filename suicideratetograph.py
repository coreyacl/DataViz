import pandas as pd
import matplotlib as plt
import numpy as np

data = pd.read_csv("files/suiciderate.csv")
df = pd.DataFrame(data)

"""
Occupations:
Plumber - 4
Surgeon - 11
Accountant - 13
Software - 15
Mech E - 17
Farming - 22
Physicist - 29
"""
def get_number_or_percent(dataframe, occupation, type):
    """Takes in the dataframe, occupation (in number form from above), and type
    which is either 
    df2 = pd.DataFrame(dataframe['Total'].values.tolist())
    print(df2.loc[occupation])
