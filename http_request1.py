from bottle import get, post, request, run

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit">
        </form>
    '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(name, password):
    if name == "admin" and password == "admin":
        return True
    else:
        return False

run(host='0.0.0.0', port=8080)
