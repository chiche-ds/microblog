from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello World</h1> "

@app.route('/about')
def about():
    return "<h1>About Page </h1>"