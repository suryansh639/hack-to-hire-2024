from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock data for flights
flights = [
    {"id": 1, "number": "AB123", "status": "On Time", "gate": "A1", "time": "12:30"},
    {"id": 2, "number": "CD456", "status": "Delayed", "gate": "B2", "time": "14:00"},
    {"id": 3, "number": "EF789", "status": "Cancelled", "gate": "C3", "time": "16:30"},
]

@app.route('/api/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    
    return jsonify({"message": "Subscribed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
