from flask import Flask, render_template

app = Flask (__name__)

def connect_db():
	return sqlite3.connect(app.database)

@app.route('/')
def homepage():
	return render_template("mainT.html")
	
@app.route('/graph')
def graph():
	return render_template("dataT.html")
	
if __name__=="__main__":
	app.run()
