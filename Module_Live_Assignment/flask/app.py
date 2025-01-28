
from flask import Flask, redirect, url_for, request, render_template
#from fileinput import filename 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

about_message = {

    "name": "My First Flask App",
    "description":"This is a basic app that displays basic login and then home page after successful login",
    "author": "Jyothi",
    "emailid": "jyothi@xyz.com",
    "version": 1.0
}

'''
Create a RESTful endpoint for fetching information about the app
about() is the conroller API
'''
@app.route('/myapp/api/v1/about')
def about():
    return about_message

@app.route('/') #homepage
def greet_world():
    return "Hello, World!"

@app.route('/greet/<name>') #homepage
def greet_name(name):
    return "Hello, %s!" %name

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name

@app.route('/auth')
def auth():
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return render_template("upload.html")
    else:
        f = request.files['file']
        fname = 'data/%s' %f.filename
        f.save(fname)
        return render_template('acknowledgement.html', name=f.filename)



if __name__ == '__main__':
    app.run(debug=True)