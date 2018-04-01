import gspread #https://github.com/burnash/gspread
#https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
from oauth2client.service_account import ServiceAccountCredentials
from pdb import set_trace #set_trace() is godsend. Used for troubleshooting

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('DataViz.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sh = client.open_by_key('1E6E1iKK38B9JyNcpqK8VpfH9nCMIZzKEyNREv_DTAO0')
worksheet = sh.get_worksheet(0)

val = worksheet.cell(1,1).value
row = worksheet.row_values(1)

set_trace()
worksheet.update_acell('B6','Ava is cool')

# print(val)
# print(row)
print('Done')
