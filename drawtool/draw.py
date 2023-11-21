import json

a=0
b=0
list=[]
for i in range(10):
    a=0
    b+=50
    if i %3 ==2:
        continue
    else:
        for n in range(10):
            a+=50
            if n %3 ==2: 
                continue
            else:
                x1 = [a,b,a+50,b+50]
                x2 = [a,b,a,b+50]
                x3 = [a,b+50,a+50,b+50]
                list.append(x1)
                list.append(x2)
                list.append(x3)


with open("drawtool.json","w",encoding="utf-8") as f:
    json.dump(list,f)


