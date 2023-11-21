import json,graphviz,sys

json_file = "toyotomi.json"

if len(sys.argv) >= 2:
    json_file=sys.argv[1]
with open(json_file,encoding="utf-8") as f:
    family_data = json.load(f)

g = graphviz.Graph("family", format="svg", filename=json_file+"_out")
g.attr("node",shape="box",dir="none")
g.attr(rankdir="TB")#上下に並べる

for f in family_data:
    print(f)
    g.attr(rankdir="TB")
    fa=f["parents"][0]
    mo=f["parents"][1] if len(f["parents"])>=2 else ""
    pp = fa +"_"+mo
    with g.subgraph() as sg:
        sg.graph_attr["rank"]="same"
        sg.node(fa,style="filled",fillcolor="#f0f0ff")
        sg.node(mo,style="filled",fillcolor="#fff0e0")
        sg.node(pp,shape="point")
        sg.edge(fa,pp,dir="none")
        sg.edge(pp,mo,dir="none")

    if len(f["children"])>0:
        pc=pp+"_pc"
        g.node(pc,shape="point")
        g.edge(pp,pc,dir="none")
        for c in f["children"]:
            g.node(c)
            g.edge(pc,c,dir="none")
            
g.view()