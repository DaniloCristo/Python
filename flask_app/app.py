from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

from data import Articles


from flask_mysqldb import MySQL

from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from passlib.hash import sha256_crypt


app = Flask(__name__)

#Config MYSQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123"
app.config["MYSQL_DB"] = "myFlaskApp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

Articles = Articles()


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/articles")
def articles():
	return render_template("articles.html", articles = Articles)


@app.route("/article/<string:id>/")
def article(id):
	return render_template("article.html", id=id)

class RegisterForm(Form):
	name = StringField("Name", [validators.Length(min = 1, max = 50)])
	user_name = StringField("UserName",[validators.Length(min=4, max=25)])
	email = StringField("Email",[validators.Length(min=6,max=50)])
	password = PasswordField("Password", [
			validators.DataRequired(),
			validators.EqualTo("confirm",message="Passwords, do not match")
		])
	confirm = PasswordField("Confirm")

@app.route("/register",methods=["GET", "POST"])
def register():
	form = RegisterForm(request.form)
	if request.method == "POST" and form.validate():
		#pegando os dados do formulario
		name = form.name.data
		user_name = form.user_name.data
		email = form.email.data
		password = sha256_crypt.encrypt(str(form.name.data))
		#confirm = form.name.data

		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO users(name,email,user_name,password) VALUES(%s, %s,%s,%s)',(name,email,user_name,password))
		mysql.connection.commit()

		cur.close()

		flash("Você esta registrado pode logar", "success")
		return redirect(url_for("index"))
	return render_template("register.html", form=form)


if __name__ == "__main__":
	app.secret_key = "secret123"
	app.run()