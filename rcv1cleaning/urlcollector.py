#!/usr/bin/env python
"""

"""
import json
import urllib


def main():
    numResults = 50
    with open('/home/ghackeling/nsp/rcv1-cleaning/data/queries.txt') as f:
        queries = f.read().splitlines()

    for query in queries:
        print '** Starting', query
        urls = get_results(query, numResults)
        out = open('/home/ghackeling/nsp/rcv1-cleaning/data/urls-%s.txt' % query.replace(' ', '-').replace('/', '-').lower(), 'w')
        for url in urls:
            out.write("%s\n" % url.encode('ascii', 'ignore'))


def get_results(query, numResults):
    counter = 0
    urls = []
    while counter < 10:
        skip = counter * numResults
        results = get_result(query, numResults, skip)
        urls.extend(results)
        counter += 1
    return urls


def get_result(query, numResults, skip):
    bing_account_key = 'dmeLVnBSkLXa2lQ7kSG0yFdNmu0CTXqvFy3Cij7uads='
    search_base_url = 'https://user:%s@api.datamarket.azure.com/Bing/Search/v1/Web?' % bing_account_key
    bingParameters = {
        "Query": "'%s'" % query,
        "Market": "'en-US'",
        "$top": numResults,
        "$format": "JSON",
        "$skip": skip
    }
    queryString = urllib.urlencode(bingParameters)
    url = search_base_url + queryString
    json_data = urllib.urlopen(url)
    results = json.load(json_data)
    return [i['Url'] for i in results['d']['results']]


if __name__ == '__main__':
    main()