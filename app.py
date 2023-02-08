from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello():
    with open('index.html') as f:
        return f.read()
    

@app.route("/home")
def home():
    return "<h1>Home page</h1>"

if __name__ == "__main__":
    app.run(port=None) 