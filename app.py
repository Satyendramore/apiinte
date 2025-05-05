from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/mydb'
mongodb = PyMongo(app).db

@app.route('/')
def hello():
    return "Hi, I am Satyendra"

@app.route('/api/v1/colleges', methods=['GET'])
def get_colleges():
    state_colleges = [
        {"id": 1, "state": "Haryana", "colleges": ["VIIT", "IIIT", "MIIIT"]},
        {"id": 2, "state": "Rajasthan", "colleges": ["LIIT", "MVIT", "CMIT"]},
        {"id": 3, "state": "UP", "colleges": ["SVIIT", "MVNIT", "VNMIT"]}
    ]
    response = {
        "status": "success",
        "count": len(state_colleges),
        "data": state_colleges
    }
    return jsonify(response)

if __name__ == "__main__":
 app.run(debug=True, host='0.0.0.0', port=5001)



