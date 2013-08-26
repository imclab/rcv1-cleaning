#!/usr/bin/env python
"""

"""
import re
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

html = urlopen('http://gavinmh.github.io/6-and-12-site/').read()
soup = BeautifulSoup(html)
texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_texts = filter(visible, texts)

out = ' '.join(visible_texts)
out.replace('\n', ' ')
out.replace('\t', ' ')

print out