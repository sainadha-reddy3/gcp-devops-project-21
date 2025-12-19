from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "GCP DevOps Project 21 - Application is running!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
