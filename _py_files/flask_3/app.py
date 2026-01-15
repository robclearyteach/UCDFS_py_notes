
from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet')
@app.route('/greet/<a_name>')
def greet(a_name=""):
        return render_template('greet.html', name=a_name)
    


if __name__ == "__main__": #if you execute this file
    app.run(debug=True)