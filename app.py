from flask import Flask,render_template

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route('/mypage/kontakt')
@app.route('/mypage/me')

def me():
    return render_template("me.html")
