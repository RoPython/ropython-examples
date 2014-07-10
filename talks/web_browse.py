#! /usr/bin/env python

""" Parse the CNN rss feed and open the most recent
10 links in the browser.
"""
 
import webbrowser
import requests

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_urls(max_urls=None):
    handle = requests.get("http://rss.cnn.com/rss/edition_technology.rss")
    soup = BeautifulSoup(handle.content)
    return [item.findAll("guid")[0].text
            for item in soup.find_all('item')][:max_urls]

executor = ThreadPoolExecutor(max_workers=3)
for url in get_urls(max_urls=3):
    executor.submit(webbrowser.open, url)
