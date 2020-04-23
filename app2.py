from flask import Flask

app2 = Flask(__name__)

@app.route('/')


def home():
    return "welcome"

if __name__ == '__main__':
    app2.run('localhost',5051)

