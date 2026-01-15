
from flask import Flask, render_template, url_for, redirect, session

app = Flask(__name__)
app.secret_key =  'put a real secret key here: this just for demo'
city_data = [
     {"id":1, "name": "New York", "latitude": 40.7128, "longitude": -74.0060}
    ,{"id":2, "name": "Los Angeles","latitude": 34.0522,"longitude": -118.2437}
]



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
    


@app.route("/visit/<int:city_id>")                      #CHANGE: add 'int:' before a_num
def visit(city_id):    
    #python code to compute digit sum of a_num
    print(f"visit(): {city_id=}")
    city_name=None                                      #bug-fix: renamed: distinct to loop 'city'
    for city in city_data:
         print(f"inside for: {city=}, {city["id"]=}, {city["name"]=}")
         if city["id"] == city_id:
              city_name = city["name"]
    return f"<h1> Enjoy your visit to: {city_name} </h1>"


if __name__ == "__main__": #if you execute this file
    app.run(debug=True)