from flask import Flask, request, send_file
import os, pyqrcode, time, html

ROOT_DIR = os.path.dirname(__file__)
PNG_FILE = os.path.join(ROOT_DIR,"qrcode.png")

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q","https://example.com")
    if q != "":
        qrcode = pyqrcode.create(q)
        qrcode.png(PNG_FILE,scale=8)
    return """
        <html><meta charset="UTF-8">
        <body>
            <p>
            <form action="/" method="GET">
                <input type="text" name="q" size="60" value="{}">
                <imput type="submit" value="生成">
            </form>
            </p>
            <img src="/qrcode.png?r={}">

        </body>        
        </html>
    """.format(html.escape(q),time.time())

@app.route("/qrcode.png")
def sed_qrcode():
    return send_file(PNG_FILE,mimetype="image/png")

if __name__ =="__main__":
    app.run("0.0.0.0", 8888, debug=True)