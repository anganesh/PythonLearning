import openpyxl
import os
import pandas as pd

from openpyxl import load_workbook
os.chdir(r"E:/github_anganesh/PythonLearning/oracle")
print (os.getcwd())

absolute_filename = r"multisheet.xlsx"
if not os.path.isfile(absolute_filename):
   print("ERROR: File not found!")
   exit(-1)
path = r"E:/github_anganesh/PythonLearning/oracle/multisheet.xlsx"

path1 = r"E:/github_anganesh/PythonLearning/oracle/mergesheet.xlsx"

   
wb= openpyxl.load_workbook(path)
writer = pd.ExcelWriter(path1, engine = 'openpyxl')

sheetname = "db"
ws = wb[sheetname]

data = ws.values
columns = next(data)[0:]
df = pd.DataFrame(data, columns=columns)
print(df.head(3))


sheetname = "analysis"
ws = wb[sheetname]

dataana = ws.values
columns = next(dataana)[0:]
dfana = pd.DataFrame(dataana, columns=columns)
print(dfana.head(3))
print("hi")

df3  = pd.merge(df, dfana, on="ID", how='left')
df3 = df3.fillna('')

print(df3.head(3))

# df3.to_excel("ExcelFile.xlsx",columns=['col1', 'col3'], sheet_name = "NewSheet1")
df3.to_excel(writer, columns=['ID', 'Name', 'Note'] ,sheet_name = 'mergedata')
writer.save()
writer.close()

