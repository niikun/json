import json,random,os
#初期設定
savefile="janken_history.json"
history = []
hand_labels = ["グー", "チョキ", "パー"]

#メイン処理
def main():
    load_history()
    while True:
        show_history()
        flagStop = janken_game()
        if flagStop: break

#じゃんけんゲーム
def janken_game():
    com = random.randint(0,2)
    user = ask_user_hand()
    if user == 3: return True
    print("you: ",hand_labels[user])
    print("com: ",hand_labels[com])
    result = (com-user+3)%3
    hantei = "あいこ"
    if result == 1: hantei = "勝ち"
    if result == 2: hantei = "負け"
    print("判定: ",hantei)
    history.append({"com":com,"user":user,"result":hantei})
    save_history()
    return False

#play履歴の読み込み
def load_history():
    global history
    if os.path.exists(savefile):
        with open(savefile,encoding = "utf-8") as f:
            history = json.load(f)

#履歴の保存
def save_history():
    with open(savefile,"w",encoding="utf-8") as f:
        json.dump(history,f,ensure_ascii=False, indent=2)

def show_history():
    cnt,win = 0,0
    for i in history:
        if i["result"] == "あいこ": continue
        if i["result"] == "勝ち": win += 1
        cnt += 1
    r = 0 if cnt == 0 else win/cnt
    print("勝率: {} ({}/{})".format(r,win,cnt))

def ask_user_hand():
    #user入力を得る
    print("---", len(history), "回目のジャンケン---")
    print("[0]グー [1]チョキ [2]パー [3]終了 ")
    user = input("どの手を出しますか？ >")
    try:
        no = int(user)
        if 0<=no <=3: return no
    except:
        pass

    return ask_user_hand()

if __name__=="__main__": main() 


#load_history

#show_history
#