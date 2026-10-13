import os
from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_KEYS = ["KEY123-ABC", "TEST-KEY-999"]

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.get_json(silent=True) or {}
    user_key = data.get('key')
    if user_key in VALID_KEYS:
        return jsonify({"status": "success", "message": "Key valid hai!"})
    else:
        return jsonify({"status": "error", "message": "Galat key!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
