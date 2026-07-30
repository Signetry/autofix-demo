import sqlite3
import flask

app = flask.Flask(__name__)


@app.route("/user")
def get_user():
    user_id = flask.request.args.get("id")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return str(cur.fetchall())
