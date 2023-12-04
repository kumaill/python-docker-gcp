from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker using new flask app on Cloud Function!!'

if __name__ == "__main__":
    app.run(debug=True)