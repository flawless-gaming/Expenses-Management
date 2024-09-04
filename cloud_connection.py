import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
     "https://www.googleapis.com/auth/drive"
         ]

creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scopes)


file = gspread.authorize(creds)
workbook = file.open("test_file")
sheet = workbook.sheet1
#print(sheet.range("A1:C1"))
#for cell in sheet.range("A1:C1"):
 #   print(cell.value)
 
#print(sheet.acell("B1").value)

#print(sheet.row_values(1))
#print(sheet.col_values(1))

#update data

#sheet.update_acell("A1","Rishi")
#print(sheet.acell("A1").value)

#sheet.update("B1:C1",[["Hemant","Jain"]])
#print(sheet.row_values(1))
