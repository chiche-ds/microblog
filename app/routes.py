from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'ChiChe'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in poland'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return "<h1>About Page </h1>" 

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)