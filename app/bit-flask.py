from flask import Flask, render_template, request
import string 
import random
import bit


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
	if request.method == 'POST':
		return render_template('hello.html', shortened_url=shorten(), original_url=request.form["url"], length=request.form["length"])
	else:
		return render_template('hello.html')

def shorten():
	try:
		length = int(request.form["length"])
	except:
		length =6
	return bit.shortenurl(request.form["url"], length)


if __name__ == "__main__":
	app.run(debug=True)

