# Web Services Automation

# The webbrowser Module

import webbrowser
url = "http://www.python.org/"
webbrowser.open(url)

# to open in a new window:

webbrowser.open_new(url)

# to open in a new tab (some browsers do this alreday via their own prefs):

webbrowser.open_new_tab(url)

# Web APIs and Representational State Transfer (REST)

# Instead of publishing web pages, you can provide data through a web
# application programming interface (API). Clients access your service by
# making requests to URLs and getting back responses containing status and
# data. Instead of HTML pages, the data is in formats that are easier for
# programs to consume, such as JSON or XML.

# Many products claim to have a REST or RESTful interface. In practice, this
# often only means that they have a web interface (definitions of URLs to
# access a web service).

# a RESTful service uses the HTTP verbs in specific ways:

# HEAD - gets information about the resource, but not its data.

# GET - retrieves the resource's data from the server. This is the standard
# method used by a browser. Any time you see a URL with a question mark (?)
# followed by a bunch of arguments, that's a GET request. GET should not be
# used to create, change, or delete data.

# POST - updates data on the server, often used by HTML forms and web APIs.

# PUT - creates a new resource

# DELETE - deletes

# A RESTful client can also request one or more content types from the server
# by using HTTP request headers. For example, a complex service with a REST
# interface might prefer its input and output to be JSON strings.

# JSON is especially well suited to web client- server data interchange.
# It's especially popular in web-based APIs, such as OpenStack.

# Crawl and Scrape

# Sometimes, you might want a little bit of information available only in HTML
# pages, surrounded by ads and extraneous content. An automated web fetcher
# (called a crawler or spider) retrieves contents from the remote web servers,
# and a scraper parses the content to find the needle in the haystack.

# If you need an industrial-strength combined crawler and scraper, Scrapy is
# worth downloading: $ pip3 install scrapy

# Scrapy is a framework, not a module. It does more, but it's more complex to
# set up. Learn more about Scrapy: https://scrapy.org

# Scrape with BeautifulSoup

# If you already have the HTML data from a website and just want to extract
# from it, BeautifulSoup is a good choice. HTML parsing is a headache because
# much of the HTML on public web pages is technically invalid: unclosed tags,
# incorrect nesting, and other complications.

# $ pip3 install beautifulsoup4

# The following example uses it to get all the links from a web page. A
# function get_links() will do most of the work, and a main program to get one
# or more URLs as command-line arguments.

def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
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
