import xlrd
import argparse
##source: https://www.sitepoint.com/using-python-parse-spreadsheet-data/##

#constructing an argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-x", "--excel", required=True,
    help="path to the input")

args = vars(ap.parse_args())

workbook = xlrd.open_workbook(args["excel"], encoding_override="cp1252") #encoding for non-ASCII characters
sheet1 = workbook.sheet_by_index(0)

#value of 1st row and first columns
print(sheet1.cell(0,0).value)
#prints column
print(sheet1.col(0))
