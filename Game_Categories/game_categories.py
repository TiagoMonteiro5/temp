from flask import Flask 

app = Flask(__name__)

@app.route("/")
@app.route("/Categories")
def home():
    return "<h1>Categories Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
