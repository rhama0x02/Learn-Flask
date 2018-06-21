from flask import Flask,render_template, request, jsonify, url_for
from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "helloworld"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        data = {"username" : username,"password" : password, \
        "remember_me" : remember_me }
        return jsonify(data)
    return render_template("login.html",form=form)

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password_confirm = form.password_confirm.data
        data = {"message" : "Success","info" :[{"username" : username,"password" : password, \
        "password_confirm" : password_confirm }]}
        return jsonify(data)
    return render_template("register.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)