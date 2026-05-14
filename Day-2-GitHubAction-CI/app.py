from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(
        {"message": "Hello DevOps!", "version": os.getenv("APP_VERSION", "1.0.0")}
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
