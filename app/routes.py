from flask import render_template
from app import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    user = {'username': 'andresroot'}

    posts = [
        {
            'author': {
                'username': 'John'
            },
            'body': 'These are my thoughts.'
        },
        {
            'author': {
                'username': 'Mary'
            },
            'body': 'These are mary\'s thoughts.'
        },
    ]

    return render_template('index.html', user=user, posts=posts)
