from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'gesture': u'me',
        'nope': u'no gesture for you lol', 
        'done': False
    },
    {
        'id': 2,
        'gesture': u'hey!',
        'nope': u'shut.', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "hi bot"

@app.route("/add-gesture", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "can you just be quiet ok?! stop trying to make me work I won't work."
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Gesture': request.json['gesture'],
        'YES?': request.json.get('nope', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "GESTURE NOT ADDED!! go get a life lol."
    })
    

@app.route("/get-gesture")
def get_task():
    return jsonify({
        "gesture" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
