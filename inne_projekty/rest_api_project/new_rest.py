from bottle import Bottle

app = Bottle()

verb = 'Hello there'
@app.route('/')
def hello():
    return verb


app.run()
