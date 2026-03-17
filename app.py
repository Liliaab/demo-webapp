from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Welcome to Lilia's Web App! <br> This is a simple application running in a Docker container hosted by aws app runer"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

