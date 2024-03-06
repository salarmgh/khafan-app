from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run()
