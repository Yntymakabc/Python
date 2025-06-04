from flask import Flask, jsonify, request
all = []
class person:
    def __init__(self, name, age):
        self.name = name
        self. age = age 
        self.cards = []

    

app = Flask(__name__)



@app.route("/")
def hello():
    return [4,5,6,7,6,5,4]

@app.route("/add")
def add_numbers():
    a = request.args.get("a", 0, type=int)  # Convert to int
    b = request.args.get("b", 0, type=int)  # Convert to int
    return str(a + b)  # Convert result back to string for response

@app.route("/create")
def create():
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    p = person(name, age)
    return jsonify({
        "status":"success", 
        "message":"successfully user was created"

    })

    
if __name__ == "__main__":
    app.run(debug=True)
