import json, graphviz

openfile = "excel-menu-norm.json"


with open(openfile,encoding="utf-8")as f:
    menus = json.load(f)

g = graphviz.Digraph("G",filename="excel-menu-norm",format="svg")
g.attr(rankdir="LR")
g.attr("node",shape="record")
g.node("menu")
mtype_dic={}

for menu in menus:
    if menu["type"] not in mtype_dic:
        mtype_dic[menu["type"]]=True
        g.edge("menu",menu["type"])
    g.edge(menu["type"],menu["name"])
    g.edge(menu["name"],str(menu["price"])+"円")


g.view()