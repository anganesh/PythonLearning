import cx_Oracle, json
import db_config
from openpyxl import Workbook



rowheader = []
rowdata = []
book= Workbook(write_only = True)
sheet = book.create_sheet()


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cur = con.cursor()

cur.execute("select * from departments")

""" below cur.description to get the column header"""

for column in cur.description:
    rowheader.append(column[0])
sheet.append(rowheader)
print(rowheader)


""" appending sql data to each row"""
    
res = cur.fetchall()
for row in res:
    rowdata.append(row)
    sheet.append(row)
print(rowdata)

book.save("departmentaz.xlsx")

#print json.dumps(rowdata, default=json_serial)

cur.close()
con.close()


