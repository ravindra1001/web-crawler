__author__ = 'ravindra'
from bs4 import BeautifulSoup
def print_link_from_sourse_code(code):
    code=BeautifulSoup(code)
    for link in code.findAll('a'):
        print(link.get('href'))

def indent(code):
    code=BeautifulSoup(code)
    print(code.prettify())

def title(code):
    code=BeautifulSoup(code)
    print(code.title)

def get_text(code):
    code = BeautifulSoup(code)
    text = code.get_text()
    print(text)

code = ''' <html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

