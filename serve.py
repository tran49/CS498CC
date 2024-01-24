from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    global seed
    if request.method == 'POST':
        subprocess.run(["python3", "stress-cpu.py"])
    else:
        return socket.gethostname()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
