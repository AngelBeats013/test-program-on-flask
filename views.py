# Core logic
# coding:utf8

from flask import Flask, render_template

app = Flask(__name__)


# Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# Register
@app.route('/register/', methods=['GET', 'POST'])
def login():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
