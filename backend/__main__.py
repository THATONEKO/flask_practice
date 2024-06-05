from backend import create_app
from flask import jsonify, request, Response
app = create_app()

# creating end points



if __name__ == "__main__":
    app.run(host="127.0.0.1")