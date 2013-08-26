#!/usr/bin/env python
"""

"""
import json
import urllib

bing_account_key = 'dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads='

# user:dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads=@api.datamarket.azure.com/Bing/Search?Query=stratocaster

# https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27web%27&Query=%27les%20paul%27

search_base_url = 'https://user:%s@api.datamarket.azure.com/Bing/Search?' \
    % bing_account_key

search_base_url = 'https://user:%s@api.datamarket.azure.com/Bing/Search/v1/Composite' % bing_account_key

numResults = 100
query = 'camping'

bingParameters = {
    "Sources:": "web",
    "Query": "'%s'" % query,
    "Market": "'en-US'",
    "$top": numResults,
    "$format": "JSON"
}
queryString = urllib.urlencode(bingParameters)
url = search_base_url + queryString
print url
json_data = urllib.urlopen(url)
results = json.load(json_data)
for i in results['d']['results']:
    print 'results:', i
