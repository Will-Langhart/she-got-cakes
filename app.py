from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to SheGotCakes!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
