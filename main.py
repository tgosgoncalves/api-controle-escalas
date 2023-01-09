from flask import Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    return 'ok'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)