from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {0}, remember_me={1}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', form=form)
