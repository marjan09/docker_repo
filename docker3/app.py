# service_b/app.py
from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/compute', methods=['GET'])
def compute():
    # Simulate a heavy computation task
    data = [1] * 10**6  # List with a million elements
    replicated_data = data * 100  # Replicating the list many times
    time.sleep(5)  # Simulate a delay in computation
    return jsonify({"message": "Computation done", "data_size": len(replicated_data)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8002)