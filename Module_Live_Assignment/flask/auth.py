from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
#import bcrypt

app = Flask(__name__)

app.secret_key = "testing"

client = MongoClient('mongodb://localhost:27017/')
db = client['demo']
users_collection = db['users']

@app.route('/')
def home():
    #return "Welcome Jyothi"
    return redirect(url_for('register'))

@app.route('/success/<name>')
def success(name):
    return 'Hello.. Welcome %s' %name

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            flash('Username already exists. You can now log in.', 'success')
        else:
            users_collection.insert_one({'username': username, 'password': password})
            flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
           
    else:
        return render_template('register.html')
    #return redirect(url_for('login'))
    #return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            #flash('Login successful.', 'success')
            #user = request.form['name']
            return redirect(url_for('success', name=username))
                        
            # Add any additional logic, such as session management
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html')    
    else:    
        return render_template('login.html')
    
    
if __name__ == '__main__':
    app.run()