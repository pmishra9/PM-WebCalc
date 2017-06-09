from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome Praveen to Beer City Code Conferece"


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/<int:a>/<op>/<int:b>')
def calc(a, op, b):
    return f"Result: {a} {op} {b} = {a + b}"
