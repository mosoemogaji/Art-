from flask import Flask, request
import os

app = Flask(__name__)

# Home route (prevents 404)
@app.route('/')
def home():
    return "App is running!"

# Example POST route (safe demo)
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')

    # Just demonstrate receiving data (no password capture)
    return f"Received email: {email} (demo only)"

# IMPORTANT: Render deployment fix
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)