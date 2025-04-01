"""
Program: Routes
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: Routes file for Flask application


Revisions:

"""


from flask import Blueprint, flash, render_template, redirect,  url_for

pages = Blueprint('pages', __name__)

@pages.route('/')
@pages.route('/index')
def index():
    head_title = 'Home'
    page_title = 'Flask Shell'
    user = {'username': 'Maya'}

    sample_data = [
        {
            'title': 'Seasons Greetings',
            'author': 'John',
            'body': 'Merry Christmas everyone!',
            'posted': '12/25/2025'

        },
        {
            'title': 'Seasons Greetings',
            'author': 'Susan',
            'body': 'A merry Christmas to you too!',
            'posted': '12/25/2025'
        },
        {
            'title': 'Seasons Greetings',
            'author': 'Maya',
            'body': 'And a Happy New Year!',
            'posted': '12/30/2025'
        },
        {
            'title': 'Seasons Greetings',
            'author': 'Bob',
            'body': 'Happy holidays',
            'posted': '12/26/2025'
        }
    ]
    return render_template('index.html',
                           head_title=head_title,
                           page_title=page_title,
                           sample_data=sample_data,
                           user = user)