from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome Praveen to Beer City Code Conferece"


if __name__ == '__main__':
    app.run(debug=True)
