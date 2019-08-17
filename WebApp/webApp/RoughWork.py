from flask import Flask, flash, redirect, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/')
def base():
    print("Blah!")
    return(" ")
    
@app.route('/index')
def index():
    user = {'username': 'Jonny Greenwood'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',  user=user, posts=posts)


if __name__ == "__main__":
    app.run()