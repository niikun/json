import json, japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

savefile = "janken_history.json"
with open(savefile,encoding="utf-8") as f:
    history = json.load(f)
print(history)

win,lose,draw =0,0,0
hand=[0,0,0]
for i in history:
    if i["result"] == "あいこ":
        draw += 1
    if i["result"] == "勝ち":
        win += 1
        hand[i["user"]] +=1
    if i["result"] == "負け":
        lose += 1
print(f"勝率 : {win/(win+lose)}")

plt.subplot(1,2,1)
plt.pie([win,lose,draw],labels=["勝ち","負け","あいこ"])
plt.title("勝ち負け")
plt.subplot(1,2,2)
plt.bar(["グー","チョキ","パー"],hand)
plt.title("どの手で勝ったか？")
plt.show()