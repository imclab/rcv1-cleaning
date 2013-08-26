#!/usr/bin/env python
"""

"""
import os
from urllib import urlopen
import hashlib
import chardet


def main():
    hashesList = []
    files = get_url_list_files()
    for file in files:
        print '** Starting file', file
        with open('/home/ghackeling/nsp/rcv1-cleaning/data/urls/%s' % file) as f:
            urls = f.read().splitlines()
            for url in urls:
                print '**** Starting URL', url
                hash = writeOut(url, urlopen(url).read())
                hashesList.append((url, hash))


def writeOut(url, document):
    encoding = chardet.detect(document)['encoding']
    if encoding is None:
        encoding = 'utf-8'
    hash = hashlib.md5(url).hexdigest()
    out = open('/home/ghackeling/nsp/rcv1-cleaning/data/pages/page-%s.txt' % hash, 'w')
    document = document.decode(encoding, 'ignore')
    out.write(document.encode('utf-8', 'ignore'))
    out.close()
    return hash


def get_url_list_files():
    os.chdir("/home/ghackeling/nsp/rcv1-cleaning/data/urls")
    files = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            files.append(file)
    return files


if __name__ == '__main__':
    main()