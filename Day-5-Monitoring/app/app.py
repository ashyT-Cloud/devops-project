cat > Day-4-CD-Pipeline/app.py << 'EOF'
from flask import Flask, jsonify
from prometheus_flask_exporter import PromtheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Static info metric - shows app version as a label
metrics.info("app_info", "Application info", version=on.getenv("APP_VERSION", "1.0.0"))

@app.route("/")
def hello():
    return jsonify(
        {"message": "Hello DevOps!", "version": os.getenv("APP_VERSION", "1.0.0"),"deployed_by": "GitHub Actions CD",}
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": os.getenv("APP_VERSION", "1.0.0"),
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
