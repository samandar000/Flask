from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello():
    return "<h1>Pardayev Samandar</h1>"
@app.route("/index")
def index():
    return "<h1>HELLO WORLD</h1>"  

@app.route("/home")
def home():
    return "<h1>Home page</h1>"

if __name__ == "__main__":
    app.run() 



# def hello():
#     with open('index.html') as f:
#         return f.read()   