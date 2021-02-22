from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news,news_from_source,get_sources, search_topic

countries_dict={
    "cn":"China",
    "fr":"France",
    "de":"Germany",
    "it":"Italy",
    "gb":"United Kingdom",
    "ru":"Russia",
    "za":"South Africa",
    "ca":"Canada",
    "il":"Israel",
    "au":"Australia",
    "nz":"New Zealand",
    "in":"India",
    "nl":"Netherlands",
    "jp":"Japan",
    "mx":"Mexico",
    "us":"United States"
}

@main.route('/')
@main.route('/home')
def index():
    top_news=get_news("us", "general")
    cnn=news_from_source("cnn")
    bbc=news_from_source("bbc-news")
    aljazeera=news_from_source("al-jazeera-english")
    usa_today=news_from_source("usa-today")
    politico=news_from_source("politico")
    cbs=news_from_source("cbs-news")
    
    newsweek=news_from_source("newsweek")
    fox=news_from_source("fox-news")
    time=news_from_source("time")
    nbc=news_from_source("nbc-news")
    reuters=news_from_source("reuters")
    msnbc=news_from_source("msnbc")

    sources=get_sources()
    topic_name = request.args.get('topic_query')

    if topic_name:
        return redirect(url_for('.news_topic', query=topic_name))

    else:
        title="Marekani"
        return render_template('index.html', title=title, breaking_news=top_news, cnn=cnn, bbc=bbc, al=aljazeera,usa_today=usa_today, politico=politico, cbs=cbs, sources=sources, newsweek=newsweek, fox=fox, time=time, nbc=nbc, reuters=reuters, msnbc=msnbc)


@main.route('/source/<id>')
def news_source(id):
    news_list=news_from_source(id)
    title=news_list[0].source_name
    sources=get_sources()
    return render_template('news_list.html', title=title, news_list=news_list, sources=sources)


@main.route('/breaking')
def breaking_news():
    breaking_news=get_news("us", "general")
    title="Breaking News"
    sources=get_sources()
    return render_template('news_list.html', title=title, news_list=breaking_news, sources=sources)


@main.route('/categories/<id>')
def news_category(id):
    category_news=get_news("us", id)
    title=id.capitalize()
    sources=get_sources()
    return render_template('news_list.html', title=title, news_list=category_news, sources=sources)


@main.route('/countries/<id>')
def news_country(id):
    country_news=get_news(id, "general")
    title=countries_dict[id]
    sources=get_sources()
    return render_template('news_list.html', title=title, news_list=country_news, sources=sources)


@main.route('/topic/<query>')
def news_topic(query):
    articles=search_topic(query)
    title="Articles: "+query
    sources=get_sources()
    return render_template('news_list.html', title=title, news_list=articles, sources=sources)