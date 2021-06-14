import cx_Oracle
import db_config
from openpyxl import Workbook



rowheader = []
rowdata = []
book = Workbook()
sheet = book.active


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cur = con.cursor()

cur.execute("select * from departments")
for column in cur.description:
    rowheader.append(column[0])
sheet.append(rowheader)
print(rowheader)


    
res = cur.fetchall()
for row in res:
    rowdata.append(row)
    sheet.append(row)
print(rowdata)

book.save("department10.xlsx")


cur.close()
con.close()


