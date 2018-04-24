import pandas as pd
import matplotlib as plt
import numpy as np

data = pd.read_excel("files/OES_Report(1).xlsx")
df = pd.DataFrame(data)


"""
This is the information to input----
    For the profession:
        0 - Accountant
        1 - Software Developer
        2 - Mech E
        3 - Physicist
        4 - Surgeon
        5 - Farmers
        6 - Plumber
    For the data you want :
        #information by column
        employment = 1
        hourly_mean_wage = 3
        annual_mean_wage = 4
        hourly_median_wage = 8
        annual_median_wage = 13
"""



def get_profession_data(dataframe, profession, info_needed):
    """
    This code will take a string that exactly matches one in the file and
    one of the variables from above. It returns the specific value asked for."""
    output = dataframe.iloc[profession, info_needed]
    return output
def get_all_data(dataframe, profession, data_wanted):
    """This is the same as the previous one, except it takes all the data that you
    want (in list form) and returns a new list with the outputs."""
    final_list = []
    for i in data_wanted:
        final_list.append(get_profession_data(dataframe, profession, i))
    return final_list

#data_wanted = [1,3,13]
#print(get_all_data(df, 2, data_wanted
print(get_profession_data(df,2,4))
