import json,graphviz,sys

def main():
    json_file="mm_idea.json"
    if len(sys.argv)>=2:
        json_file=sys.argv[1]

    with open(json_file,encoding="utf-8") as f:
        idea = json.load(f)
    print(idea)

    g = graphviz.Digraph("idea",engine="fdp",
                         format="svg",filename="json_file_out")
    draw_obj(g, "", idea, 0)
    g.view()

def draw_obj(g, root, node, level):
    shape="box"
    if level==0: shape="doublecircle"
    elif level==1: shape="oval"
    g.node(node["idea"],shape=shape)
    if root != "": g.edge(root,node["idea"])
    if "children" in node:
        for i in node["children"]:
            draw_obj(g, node["idea"], i,level+1)

main()
