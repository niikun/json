import json, csv

infile="excel-menu-norm.csv"
outfile="excel-menu-norm.json"
items = []

with open(infile,"r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        if i==0:continue
        name, price, type =row
        menu = {
            "name":name,
            "price":int(price),
            "type":type
        }
        items.append(menu)

json_s = json.dumps(items, indent=4, ensure_ascii=False)

with open(outfile,"w",encoding="utf-8") as f:
    f.write(json_s)

