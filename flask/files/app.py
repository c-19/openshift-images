from flask import Flask

app = Flask(__name__)


@app.route('/<data>')
def hello_world(data):
    return data


if __name__ == '__main__':
    app.run()
