from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"] ) 
def index():
    if request.method == "POST":
        user_name = request.form.get('name')
        post_msg = f"POST: name is: {user_name}"
        return render_template('index.html', msg=post_msg)
    elif request.method == "GET":
        user_name = request.args.get('name')
        get_msg = f"GET: name is: {user_name}"
        return render_template('index.html', msg=get_msg)
   
if __name__ == '__main__':
    app.run(debug=True, port=8080)
