from backend import create_app
from flask import jsonify, request, Response
app = create_app()

# creating end points
@app.route("/health", methods=["GET"])
def health_check():
    return "ok"

@app.route("/users", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "bob"}, {"id": 2, "name": "joe"}]
    return jsonify(all_users)

@app.route("/users", methods=["POST"])
def create_user():
    d = request.json
    print(d)
    return Response(status=204)


if __name__ == "__main__":
    app.run(host="127.0.0.1")