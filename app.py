from flask import flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi!"

@app.rout('/health')
def health():
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)