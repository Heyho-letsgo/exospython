from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
@app.route('/hello/Andy')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)



def hello():
    return "Hello World!"




run(app, host='localhost', port=8080)