from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Lilia Web App! This is a simple  application running in a Docker container."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
