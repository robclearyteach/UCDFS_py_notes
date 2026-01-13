
from flask import Flask, render_template, url_for

app = Flask(__name__)
city_data = [
     {"id":1, "name": "New York", "latitude": 40.7128, "longitude": -74.0060}
    ,{"id":2, "name": "Los Angeles","latitude": 34.0522,"longitude": -118.2437}
]


@app.route("/visit/<int:city_id>")                      #CHANGE: add 'int:' before a_num
def visit(city_id):    
    #python code to compute digit sum of a_num
    city=None
    for city in city_data:
         if city["id"] == city_id:
              city = city["name"]
    return f"<h1> Enjoy your visit to: {city} </h1>"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet')
@app.route('/greet/<a_name>')
def greet(a_name=""):
        return render_template('greet.html', name=a_name)
    



if __name__ == "__main__": #if you execute this file
    app.run(debug=True)