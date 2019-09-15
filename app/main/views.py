from flask import render_template
from . import main

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to best News Website Online'

    return render_template('index.html', sources = news_sources, title = title, Categories = NewCategories, Languages = NewLanguages, sort_type = sort_type, headlines = top_headlines)
