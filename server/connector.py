from flask import Flask, request, jsonify
from flask_cors import CORS
# import cors from "cors"
app = Flask(__name__)
CORS(app) 

@app.route('/receive_data', methods=['POST'])
def receive_data():
    # data = request.json
    data = request.json
      # Receive data from JavaScript
    # Process data
    print("Received data in Python:", data)  
    # For demonstration, just send back the received data
    return jsonify(data)

if __name__ == '__main__':
    # app.use(cors())
    app.run(debug=True)
