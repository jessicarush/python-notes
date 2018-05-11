'''Web Automation: Scraping'''


# The webbrowser Module
# -----------------------------------------------------------------------------

import webbrowser
url = "http://www.python.org/"
webbrowser.open(url)

# to open in a new window:

webbrowser.open_new(url)

# to open in a new tab (some browsers do this already via their own prefs):

webbrowser.open_new_tab(url)


# Crawl and Scrape
# -----------------------------------------------------------------------------
# Sometimes, you might want a little bit of information available only in HTML
# pages, surrounded by ads and extraneous content. An automated web fetcher
# (called a crawler or spider) retrieves contents from the remote web servers,
# and a scraper parses the content to find the needle in the haystack.

# If you need an industrial-strength combined crawler and scraper, Scrapy is
# worth downloading: $ pip3 install scrapy

# Scrapy is a framework, not a module. It does more, but it's more complex to
# set up. Learn more at: https://scrapy.org


# Scrape with BeautifulSoup - basic parsing example
# -----------------------------------------------------------------------------
# If you already have the HTML data from a website and just want to extract
# from it, BeautifulSoup is a good choice. HTML parsing is a headache because
# much of the HTML on public web pages is technically invalid: unclosed tags,
# incorrect nesting, and other complications.

# $ pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup as soup


r = requests.get('http://pythonhow.com/example.html')
c = r.content                              # the entire source code
s = soup(c, 'html.parser')                 # feed the content to the bs4 parser
a = s.find('div',{'class': 'cities'})      # returns the first div
a = s.find_all('div',{'class': 'cities'})  # returns a list of all divs

# print(s.prettify)

print(type(r))                      # <class 'requests.models.Response'>
print(type(c))                      # <class 'bytes'>
print(type(s))                      # <class 'bs4.BeautifulSoup'>
print(type(a))                      # <class 'bs4.element.ResultSet'>
print(type(a[2]))                   # <class 'bs4.element.Tag'>
print(a)                            # prints all the divs and their contents
print(a[2])                         # prints the 3rd div and its contents
print(a[0].find_all('h2'))          # list of all the h2 tags from the 1st div
print(a[0].find_all('h2')[0])       # just the 1st h2
print(a[0].find_all('h2')[0].text)  # just the text inside the h2 tag

for item in a:
    print(item.find_all('h2'))
# [<h2>London</h2>]
# [<h2>Paris</h2>]
# [<h2>Tokyo</h2>]

for item in a:
    print(item.find_all('h2')[0].text)
# London
# Paris
# Tokyo


# Scrape with BeautifulSoup - links example
# -----------------------------------------------------------------------------
# The following example uses it to get all the links from a web page. A
# function get_links() will do most of the work, and a main program to get one
# or more URLs as command-line arguments.

import requests
from bs4 import BeautifulSoup as soup


def get_links(url):
    result = requests.get(url)
    page = result.text
    doc = soup(page, 'html.parser')
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print ('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()

# The 'a' and 'href' represent the literal HTML: <a href="http://...">

# The above can be saved as a program and run like so:
# python3 getlinks.py http://python.org
