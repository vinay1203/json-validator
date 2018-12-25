from flask import Flask 
from flask import render_template,request,flash
from flask import redirect, url_for
from flask import json

app = Flask(__name__)
app.config['SECRET_KEY']='e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


#Main Page for the site
@app.route("/")
def index():
	return render_template('index.html')

#Need to validate and json the data that is taken from the textarea..
@app.route("/jsonify_data", methods=["POST"])
def jsonify_data():
	json_val=request.form['json_txt']
	try:
		json_object=json.loads(json_val)
		return render_template('json.html',json_object=json_object)
	except ValueError:
		flash("Looks like not a valid json text")
		return redirect(url_for('index'))
	json_object=json.loads('json_val')
	return render_template('json.html', json_object=json_object)

if __name__=="__main__":
	app.run(host="localhost", port=5004, debug=True)