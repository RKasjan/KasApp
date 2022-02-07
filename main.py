from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello"
	
@app.route("/hello")
@app.route("/hello/<planet>")
def helloWorld(planet=None):
	return render_template("index.html", planet=planet)
	
if __name__ == "__main__":
	app.run(host="0.0.0.0")
