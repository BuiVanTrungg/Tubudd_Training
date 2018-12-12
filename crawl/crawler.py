from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, baseUrl, pageUrl):
        super().__init__()
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseUrl, value)
                    self.links.add(url)
    
    def page_link(self):
        return self.links
    
    def error(self, message):
        pass

# finder = LinkFinder()
# finder.feed('<html><head><title>test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')
