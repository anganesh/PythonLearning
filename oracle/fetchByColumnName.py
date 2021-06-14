import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cur = con.cursor()
cur.execute("select department_id,department_name from departments order by department_id")
for department_id, department_name in cur:
    print("Department number: ", department_id)
    print("Department name: ", department_name)

