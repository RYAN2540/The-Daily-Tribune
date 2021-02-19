from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
@main.route('/home')
def index():
    title='The Daily Tribune'
    return render_template('index.html', title=title)