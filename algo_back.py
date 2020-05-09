from flask import Flask,request, render_template
app = Flask(__name__)


@app.route('/') #this is for our home page as it is the root aka '/'
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)
