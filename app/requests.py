import urllib.request, json
from .models import NewsArticle, Sources

api_key=None

def configure_request(app):

    global api_key
    api_key=app.config['NEWS_API_KEY']


def get_breaking_news():

    get_breaking_url = 'http://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_breaking_url) as url:
        get_breaking_data = url.read()
        get_breaking_response = json.loads(get_breaking_data)

        breaking_results = None

        if get_breaking_response['articles']:
            breaking_results_list = get_breaking_response['articles']
            breaking_results = process_breaking_results(breaking_results_list)


    return breaking_results


def process_breaking_results(breaking_list):    

    breaking_results = []

    for breaking_item in breaking_list:
        source = breaking_item.get('source')
        source_name= source['name']
        author = breaking_item.get('author')
        if author==None:
            author=source_name
        elif len(author)>40:
            author=source_name
        elif author[0:4]=="http":
            author=source_name
        title = breaking_item.get('title')
        url = breaking_item.get('url')
        image_url = breaking_item.get('urlToImage')        
        published_at = breaking_item.get('publishedAt')
        day=published_at[0:10]
        time=published_at[11:16]
        published=day+" "+time+"hrs"

        breaking_object = NewsArticle(source_name,author,title,url,image_url,published)
        breaking_results.append(breaking_object)        

    return breaking_results


def news_from_source(source_id):

    get_breaking_url = 'http://newsapi.org/v2/everything?sources={}&pageSize=30&apiKey={}'.format(source_id, api_key)

    with urllib.request.urlopen(get_breaking_url) as url:
        get_breaking_data = url.read()
        get_breaking_response = json.loads(get_breaking_data)

        breaking_results = None

        if get_breaking_response['articles']:
            breaking_results_list = get_breaking_response['articles']
            breaking_results = process_breaking_results(breaking_results_list)


    return breaking_results

def get_sources():

    get_sources_url = 'https://newsapi.org/v2/sources?country=us&category=general&language=en&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)


    return sources_results


def process_sources_results(sources_list):

    sources_results=[]

    for source in sources_list:
        source_id=source.get('id')
        source_name=source.get('name')

        source_obj=Sources(source_id, source_name)
        sources_results.append(source_obj)

    return sources_results