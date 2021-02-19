import urllib.request, json

api_key=None

def configure_request(app):
    global api_key
    api_key=app.config['NEWS_API_KEY']