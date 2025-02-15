# service_a/app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/start-computation', methods=['GET'])
def start_computation():
    # Services to which the computation requests are sent
    services = [
        'http://docker2.docker_container_namespace:8001/compute',
        'http://docker3.docker_container_namespace:8002/compute',
        'http://docker4.docker_container_namespace:8003/compute',
        'http://docker5.docker_container_namespace:8004/compute'
    ]
    


    results = []
    for service in services:
        try:
            response = requests.get(service, timeout=3000)
            if response.status_code == 200:
                results.append(response.json())
        except requests.exceptions.RequestException as e:
            results.append({"error": f"Failed to connect to {service}: {str(e)}"})

    return jsonify({"status": "computation started", "results": results})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)