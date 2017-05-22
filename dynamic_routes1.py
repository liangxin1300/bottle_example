from bottle import Bottle, run, template

app = Bottle()

@app.route('/wiki/<pagename>')
def show_wiki_page(pagename):
    return template('<b>show wiki {{pagename}}</b>', pagename=pagename)

@app.route('/<action>/<user>')
def user_api(action, user):
    return 'aciton: %s user: %s' % (action, user)

run(app, host='0.0.0.0',  port=8080)
