import cx_Oracle, json
import db_config



rowheader = []
rowdata = []


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cur = con.cursor()

cur.execute("select * from departments")
r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
json_output = json.dumps(r)

print(json_output)




print("")
print("another method to fetch data")
print("")

qry = "Select employee_id,first_name,last_name from hr.employees where rownum < 6"
# Assumes conn is a database connection.
cur.execute(qry)
rows = [x for x in cur]
cols = [x[0] for x in cur.description]
emps = []
for row in rows:
  emp = {}
  for prop, val in zip(cols, row):
    emp[prop] = val
  emps.append(emp)
# Create a string representation of your array of employees.
empsJSON = json.dumps(emps)
print(empsJSON)



""" below cur.description to get the column header

for column in cur.description:
    rowheader.append(column[0])
print(rowheader)



    
res = cur.fetchall()
print (res)
for row in res:
    rowdata.append(row)
print(rowdata)

type(rowdata)
type(res)
print("json conversion:")
json.dumps(res)
print json.dumps(res, default=json_serial)"""

cur.close()
con.close()


