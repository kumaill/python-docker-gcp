# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Docker using new flask app on Cloud Function!!'

# if __name__ == "__main__":
#     app.run(debug=True)

import functions_framework

# Register an HTTP function with the Functions Framework
@functions_framework.http
def my_http_function(request):
  print("Hello World")
  # Return an HTTP response
  return 'OK'