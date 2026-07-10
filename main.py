from flask import Flask, request

app = Flask(__name__)

# Home page with a form
@app.route('/')
def home():
    return '''
    <h2>Login Page (Demo)</h2>
    <form action="/login" method="post">
        Email: <input type="text" name="email"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    '''

# Login handler
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Email: {email}")
    print(f"Password: {password}")

    return "Login received (demo)"

# Render fix
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)