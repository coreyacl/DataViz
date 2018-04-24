import xlrd
import argparse
import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext
import matplotlib.patches as patches
import matplotlib
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
##source: https://www.sitepoint.com/using-python-parse-spreadsheet-data/##

#constructing an argument parse
#ap = argparse.ArgumentParser()
#ap.add_argument("-x", "--excel", required=True,
#    help="path to the input")

#args = vars(ap.parse_args())


workbook = xlrd.open_workbook('files/state_data/physicist.xlsx', encoding_override="cp1252") #encoding for non-ASCII characters
sheet1 = workbook.sheet_by_index(0)


#extracting the data for each state
employment = sheet1.col_values(1, start_rowx=6)

employment_im = employment[0:-6] #-6 for farmer

#converting the values to integers
employment_im = list(map(int, employment_im))
print(len(employment_im))
print(type(employment_im[0]))
#farmers don't have DC data or virginia data
def create_table():
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE','DC', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    x_pos = np.arange(len(states))
    plt.bar(x_pos, employment_im, align='center', alpha=0.5)
    plt.xticks(x_pos, states)
    plt.show()


create_table()
