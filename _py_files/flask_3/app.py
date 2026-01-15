from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/')
@app.route('/<a_name>')
def home(a_name=None):
    return render_template('index.html', name=a_name)



@app.route('/greet')
@app.route('/greet/<a_name>')
def greet(a_name=""):
        return redirect(url_for('home', a_name=a_name))  #use url_for()

    


if __name__ == "__main__": #if you execute this file
    app.run(debug=True, port=8000)
