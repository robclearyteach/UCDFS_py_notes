from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        name = request.form.get('name', 'default-value')

        return f'Hello, {name}! This is a POST request.'
    else:
        # return render_template('index.html', args=request.args)
        return render_template("index.html", title='XXX')

if __name__ == '__main__':
    app.run(debug=True)
