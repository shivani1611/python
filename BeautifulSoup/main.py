#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

def retrieve_article_list_dom( url ):

    full_url = url + "/?adid=TMZ_Web_Nav_News"
    r = requests.get( full_url )

    soup = BeautifulSoup( r.content, "html.parser" )

    articles = soup.find_all( "article", {"class":"news"} )

    for article in articles:
        print article["data-guid"]
