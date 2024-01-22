from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET', 'POST'])
def handle_seed():
    global seed_value

    if request.method == 'POST':
        data = request.get_json()
        if 'num' in data:
            seed_value = int(data['num'])
            return jsonify({"message": "Seed updated successfully"})
        else:
            return jsonify({"error": "Invalid request format"}), 400

    elif request.method == 'GET':
        return str(seed_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
