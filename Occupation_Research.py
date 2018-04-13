""" Data Visualization
authors @ coreyacl, allisonbusa, junwonlee5

This file will host the main for the Visualization.

"""

def pullData():
    """
    pulls data and stores is into something usable.
    """
    import gspread #https://github.com/burnash/gspread
    #https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
    from oauth2client.service_account import ServiceAccountCredentials
    from pdb import set_trace #set_trace() is godsend. Used for troubleshooting

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('DataViz.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    sh = client.open_by_key('1E6E1iKK38B9JyNcpqK8VpfH9nCMIZzKEyNREv_DTAO0').sheet1
    #worksheet = sh.get_worksheet(0)
    list_of_hashes = sh.get_all_records()
    print(list_of_hashes)
    #val = worksheet.cell(1,1).value
    #row = worksheet.row_values(1)

    #worksheet.update_acell('B6','dogs are cute')

    # print(val)
    # print(row)
    print('Done')
