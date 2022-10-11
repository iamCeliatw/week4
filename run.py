from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session, url_for

app = Flask(
    __name__,
    static_folder="static/",
    static_url_path="/"
)

#設定session 密鑰
app.secret_key= "asd24680"

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "POST":
        result = request.form['variable']
        return redirect(url_for("square", number=result))
    return render_template("index2.html")

#驗證系統路由 使用POST
@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        user_account = request.form['account']
        user_password = request.form['password']
    if user_account == "test" and user_password == "test":
        session['ac'] = user_account
        session['pa'] = user_password
        return redirect("/member")
    elif user_account == "" or user_password == "":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

#成功登入頁
@app.route("/member")
def member():
    if session['ac'] and session["pa"]:
        return render_template("success.html")
    else:
        return redirect("/")

#失敗登入頁
@app.route("/error")
def error():
    data = request.args.get('message')
    return render_template("error.html", data=data)

#成功登出頁
@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")

@app.route("/square/<int:number>")
def square(number):
    result = str(number ** 2)
    return render_template("result.html", data=result)


if __name__ == '__main__':
    app.run(port=3000, debug=True)