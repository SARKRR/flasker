from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')

#def index():
	#return "<h1>Hello World!</h1>"

def index():
	first_name='Sarang'
	stuff='Flask is damn good'
	favourite_pizza=['Peperoni','cheese',41]
	return render_template("index.html",first_name=first_name,stuff=stuff,favourite_pizza=favourite_pizza)


# localhost:5000/user/sarang
@app.route("/user/<name>")
def user(name):
	return render_template("user.html",user_name=name)

#Custom error pages

#invalid Server error
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500