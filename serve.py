from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    global seed
    if request.method == 'POST':
        subprocess.Popen(["python", "stress_cpu.py"])
        return jsonify({"message": "Stressing CPU in a separate process"})

    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({"private_ip": private_ip})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
