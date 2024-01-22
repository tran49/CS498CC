from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

def stress_cpu():
    # Run stress_cpu.py as a separate process
    subprocess.Popen(["python", "stress_cpu.py"])

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Create a separate process for stressing CPU
        stress_cpu()
        return jsonify({"message": "Stressing CPU in a separate process"})

    elif request.method == 'GET':
        # Return private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({"private_ip": private_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
