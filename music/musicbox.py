from flask import Flask, request, redirect
import json, os, platform, subprocess
import json2midi

root = os.path.dirname(__file__)
logfile = os.path.join(root, "musicbox.json")
midifile = os.path.join(root,"musicbox.midi")
print(f"midi_file={midifile}")
app = Flask(__name__)

@app.route("/")
def index():
    return make_top_page_html()

@app.route("/play")
def form_write():
    gakufu = []
    for row in range(32):
        c = int(request.args.get("g"+str(row), "-1"))
    note = (12*5+c) if c!=-1 else -1

    with open(logfile, "w",encoding="utf-8") as f:
        json.dump(gakufu, f)
    json2midi.save_to_midi(gakufu,midifile)
    play_midi(midifile)
    return redirect("/")

def play_midi(midifile):
    if platform.system() == "Windows":
        os.system(midifile)
    else:
        cmd = ["timidity","midfile"]
        subprocess.call(cmd)

def make_top_page_html():
    w,g = ("white","gray")
    colors = [w,g,w,g,w,w,g,w,g,w,g,w]
    mbox = "<table>"
    for row in range(32):
        s = "<tr>"
        for col in range(24):
            s += '''
            <td style="backgroud-color:{};" border=1>
                <input type="radio" mame="g{}" value="{}">
            </td>
            '''.format(colors[col%12], row, col)
        mbox += s + "</tr>\n"
        if row % 8 == 7: mbox += "<tr><td colspan='24'><tr>"
    mbox += "</table>"
    return '''
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>オルゴール</title>
            </head>
            <body>
                <h1>オルゴール</h1>
                <form action="/play" method="GET">
                <input type="submit" value="再生"><br>{}
                </form>
            </body>
            </html>
    '''.format(mbox)

if __name__ == "__main__":
    app.run("127.0.0.1",8888,debug=True)
        



