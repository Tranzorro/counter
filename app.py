from flask import Flask, render_template, session
from flask.wrappers import Response
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
counter = 1
@app.route('/')
def index():
    global counter
    counter += 1
    session["counter"] = counter
    return render_template("index.html")
@app.route('/clear', methods=['GET', 'POST'])
def clear_count():
    session.pop("counter")
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)