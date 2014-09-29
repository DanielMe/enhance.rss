import json
from urllib.request import urlopen
from yattag import Doc

def get_news(sub):
    response = urlopen("http://www.reddit.com/r/"+sub+"/new.json")
    text = response.read()
    return json.loads(text.decode("utf-8"))

def gen_rss(sub):
    data = get_news(sub)["data"]["children"]

    doc, tag, text = Doc().tagtext()
    with tag('rss', version="2.0"):
        with tag('channel'):
            with tag('title'):
                text("Enhanced Newsfeed for /r/"+sub)
            with tag('description'):
                text("foobar")
            with tag('link'):
                text("http://reddit.com/r/haskell")
        for entry in data:
            with tag('item'):
                with tag('title'):
                    text(entry['data']['title'])
    return doc.getvalue()
