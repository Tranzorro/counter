from flask import Flask, render_template, session
from flask.wrappers import Response
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")
@app.route('/clear', methods=['GET', 'POST'])
def clear_count():
    # session.pop("counter")
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)