from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eugeny Bobylev'}
    tasks = [
        {'descr': 'Создать приложение flask'},
        {'descr': 'Использовать templates'}
    ]
    return render_template('index.html', user=user, tasks=tasks)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Вход')
