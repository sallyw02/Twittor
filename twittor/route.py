from flask import render_template, redirect, url_for
from twittor.forms import LoginForm
from twittor.models import User, Tweet


def index():  # hassle to return whole html -> need ninja template
    name = {'username': 'root'}
    posts = [
        {
            'author': {'username': 'root'},
            'body': "hi I'm root!"
        },
        {
            'author': {'username': 'test'},
            'body': "hi I'm test!"
        },
    ]
    return render_template('index.html', name=name, posts=posts)


def login():
    # disable safety mechanism that requires secret key
    form = LoginForm(meta={'csrf': False})

    # when form is submitted/POST method triggered
    if form.validate_on_submit():  # if signed in successfully, go back to home page
        msg = "username={}, password={}, remember_me{}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data
        )
        print(msg)  # means user data passed to backend
        # return redirect('/')
        # helps when endpoint name for index page changes e.g. /index not /
        return redirect(url_for('index'))
        # 'index' = the 2nd param in init's add_url_rule

    # form not submitted
    return render_template('login.html', title="Sign In", form=form)
