import json
  
# Opening JSON file
f = open('sqllist.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
sheetnames = list(data.keys())
print(sheetnames)
  
# Iterating through the json
# list
for i in data['sql_details']:
    vsheetname = i["sheetName"]
    print(vsheetname)
    vsql = i["sql"]
    print(vsql)

  
# Closing file
f.close()
