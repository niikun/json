import json,graphviz,sys

json_file = "tokugawa.json"

if len(sys.argv) >= 2:
    json_file=sys.argv[1]
with open(json_file,encoding="utf-8") as f:
    family_data = json.load(f)

g = graphviz.Graph("family", format="svg", filename=json_file+"_s")
g.attr(rankdir="LR")#横向きの図にする

for f in family_data:
    print(f)
    father=f["parents"][0]
    mother=f["parents"][1] if len(f["parents"])>=2 else ""
    children = f["children"]
    g.node(father,style="filled",fillcolor="#f0f0ff",shape="box")
    fa_mo = father + "_" + mother
    g.node(fa_mo,shape="point")
    g.edge(father,fa_mo,"父",dir="none")
    if mother != "":
        g.node(mother,style="filled",fillcolor="#fff0e0")
        g.edge(fa_mo,mother,"母",dir="none")
    for child in children:
        g.node(child,style="filled",fillcolor="#f0f0ff",shape="box")
        g.edge(fa_mo,child,"子",dir="forward")
g.view()