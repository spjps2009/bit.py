from flask import Flask, render_template, request
import string 
import random
import bit


app = Flask(__name__)

@app.route("/")

def index():
	return render_template('hello.html')
@app.route("/", methods=['POST'])
def shorten():
	try:
		length = int(request.form["length"])
	except:
		length =6
	return bit.shortenurl(request.form["url"], length)


if __name__ == "__main__":
	app.run(debug=True)

