from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet_name(name):
    return "Hello %s" %name

if __name__ == '__main__' :
    app.run()