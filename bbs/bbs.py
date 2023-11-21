from flask import Flask, request, redirect
import json, os, time, html
from datetime import datetime

logfile = "bbs_log.json"
logdata = {"lastid":0, "logs":[]}
app = Flask(__name__)

@app.route("/")
def index():
    return make_top_page_html()

@app.route("/write")
def form_write():
    name = request.args.get("name","")
    msg = request.args.get("msg","")
    if name == "" or msg == "": return "パラメータの指定エラー"
    append_log({"name":name,"msg":msg,"time":time.time()})
    return redirect("/") 

def load_log():
    global logdata
    if os.path.exists(logfile):
        with open(logfile, encoding="utf-8") as f:
            logdata = json.load(f)

def append_log(record):
    logdata["lastid"] += 1
    record["id"] = logdata["lastid"]
    print(record)
    logdata["logs"].append(record)

    try:
        with open(logfile, "w", encoding="utf-8") as f:
            json.dump(logdata, f, ensure_ascii=False, indent=4)
    except Exception as e:
        return f"エラー: ファイルの書き込みに失敗しました ({e})"

def make_logs():
    s = ""
    for log in reversed(logdata["logs"]):
        name = html.escape(log["name"])
        msg = html.escape(log["msg"])
        t = datetime.fromtimestamp(log["time"]).strftime("%m/%d %H:%M")
        s += '''
        <div class="box">
            <div class="has-text-info">({}) {} さん</div>
            <div>{}</div>
            <div class="has-text-right is-size-7">{}</div>
        </div>
        '''.format(log["id"], name, msg, t)
    return s

def make_top_page_html():
    logs_html = make_logs() 
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>掲示板</title>
        <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    </head>
    <body>
    <!-- タイトル -->
    <div class="hero is-dark"><div class="hero-body">
        <h1 class="title">掲示板</h1>
    </div></div>
    <!--書き込みフォーム-->
    <form class="box" action="/write" method="GET">
    <div class="field">
        <label class="label">お名前: </label>
        <div class="controll">
            <input class="input" type="text" name="name">
        </div>
    </div>
    <div class="field">
        <label class="label">メッセージ: </label>
        <div class="controll">
            <input class="input" type="text" name="msg">
        </div>
    </div> 
    <div class="field">
        <div class="controll">
            <input class="button is-primary" type="submit" value="投稿">
        </div>
    </div>
    </form>
    '''+make_logs() + '''</body></html>'''

if __name__ == "__main__":
    load_log()
    app.run("127.0.0.1",8888,debug=True)

