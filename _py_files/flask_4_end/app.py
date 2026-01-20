from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)

app.secret_key = "put a real secret key here"

@app.route('/', methods=["GET"]) 
def index():
    """
    Below: if session is empty (i.e. first visit '/')
    
    fname and lname have None value 
    then:
    {%if fname%}
    fails in the Jinja template
    """
    print(session)
    first = session.get('user_firstname')
    last  = session.get('user_lastname')
    return render_template("index.html", fname=first, lname=last)


@app.route('/login', methods=["GET", "POST"]) 
def login():
    if request.form:
            first = request.form.get('first')
            last  = request.form.get('last')

            session['user_firstname']= first
            session['user_lastname'] = last
            return redirect( url_for("index") )
    else:
        return render_template("login.html")        #form empty

if __name__ == '__main__':
    app.run(debug=True, port=8080)



# @app.route('/', methods=["GET","POST"]) 
# def index():
#         if request.method == 'GET':
#             if request.args:
#                 first = request.args.get('first')
#                 last  = request.args.get('last')
#                 return render_template("index.html", fname=first, lname=last)
#             else: 
#                 return render_template("index.html")

#         elif request.method == 'POST':
#             print(request.form)
#             return render_template("index.html", text=f"POST: {request.form}")