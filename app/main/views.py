from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_breaking_news,news_from_source,get_sources

@main.route('/')
@main.route('/home')
def index():
    breaking_news=get_breaking_news()
    cnn=news_from_source("cnn")
    bbc=news_from_source("bbc-news")
    aljazeera=news_from_source("al-jazeera-english")
    usa_today=news_from_source("usa-today")
    politico=news_from_source("politico")
    cbs=news_from_source("cbs-news")

    abc=news_from_source("abc-news")
    fox=news_from_source("fox-news")
    time=news_from_source("time")
    nbc=news_from_source("nbc-news")
    reuters=news_from_source("reuters")
    msnbc=news_from_source("msnbc")

    sources=get_sources()
    title="Marekani"
    return render_template('index.html', title=title, breaking_news=breaking_news, cnn=cnn, bbc=bbc, al=aljazeera,usa_today=usa_today, politico=politico, cbs=cbs, sources=sources, abc=abc, fox=fox, time=time, nbc=nbc, reuters=reuters, msnbc=msnbc)


@main.route('/source/<id>')
def news_source(id):
    news_list=news_from_source(id)
    title=news_list[0].source_name
    sources=get_sources()
    return render_template('news_source.html', title=title, news_list=news_list, sources=sources)