from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(app, host='0.0.0.0', port=8080)
