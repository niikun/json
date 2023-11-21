import json, graphviz

g = graphviz.Digraph("abc",format="svg",filename="abc")

g.node("A")
g.node("B")
g.node("C")

g.edge("A","B")
g.edge("A","C")
g.view()