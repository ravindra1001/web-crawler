import urllib
import urllib.request
from bs4 import BeautifulSoup
import links_in_sourse_code
def get_page_sourse(url):
    url = urllib.request.urlopen(url)
    sourse = url.read()
    return sourse

def find_next_pages_links(sourse):
    link_list = []
    soup = BeautifulSoup(sourse)
    a = soup.findAll('a')
    for link in a:
        link_list.append(link.get('href'))
        print(link.get('href'))
    return link_list


def web_crawl(url,max_pages):
    link_list = [url]
    pages = 0
    sourse = get_page_sourse(url)
    while pages < max_pages:
        for link in find_next_pages_links(get_page_sourse(url)):
            sourse = get_page_sourse(link)
            link_list.append(link)

            print(link)
        pages += 1
        url = link_list.pop()

def plain_text(url):
    sourse = get_page_sourse(url)
    s = BeautifulSoup(sourse)
    print(s.get_text())

def start():
    print('\n\nWHAT DO U WANT:')
    print('1. crawl a page')
    print('2. analyze a page by sourse code')

    response  = int(input())

    if response == 1:
        print('\n\nwhat do u want:')
        print('1.page title:')
        print('2.page links')
        print('3.plain text')
        print('4.indent page sourse')

        task = int(input())
        if task == 1:
            url=input('Enter url:')
            code = urllib.request.urlopen(url)
            soup = BeautifulSoup(code)
            print(soup.title())
            start()
        if task == 2:
            url=input('Enter url:')
            max_page = int(input('max page:'))
            web_crawl(url,max_page)
            start()

        if task == 3:
            url=input('Enter url:')
            code = urllib.request.urlopen(url)
            soup = BeautifulSoup(code)
            print(soup.get_text())
            start()
        if task == 4:
            url=input('Enter url:')
            code = urllib.request.urlopen(url)
            soup = BeautifulSoup(code)
            print(soup.prettify())
            start()
    if response == 2 :
        print('what do u want:')
        print('1.page title:')
        print('2.page links')
        print('3.plain text')
        print('4.indent page sourse')
        task = int(input())
        if task == 1:
            links_in_sourse_code.title(links_in_sourse_code.code)
            start()
        if task == 2:
            links_in_sourse_code.print_link_from_sourse_code(links_in_sourse_code.code)
            start()
        if task == 3:
            links_in_sourse_code.get_text(links_in_sourse_code.code)
            start()
        if task == 4:
            links_in_sourse_code.indent(links_in_sourse_code.indent(links_in_sourse_code.code))
            start()
start()
