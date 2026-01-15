
from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def home():                                                     	#remove name=None parameter
    print(session)
    a_name = session.get("name", None)                            	#default to None if not exists
    return render_template("index.html", name=a_name)        	    #pass data to Jinja templating

@app.route('/greet')
@app.route('/greet/<a_name>')
def greet(a_name=None):
        session['name'] = a_name
        return redirect( url_for('home') )
    


if __name__ == "__main__": #if you execute this file
    app.run(debug=True)