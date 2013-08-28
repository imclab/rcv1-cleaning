#!/usr/bin/env python
"""

"""
import os
import re
import chardet
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(filename, html):
    s = MLStripper()
    try:
        s.feed(html)
        return s.get_data()
    except Exception:
        print 'failed to parse document', filename
        return html


def main():
    filenames = get_filename_list()
    for filename in filenames:
        print '** starting document', filename
        document = open_file(filename)
        document = re.sub(r'&#x[a-z0-9][a-z0-9];', '', document)
        document = strip_tags(filename, document)
        # document = re.sub(r'<.+>', '', document)
        # document = re.sub(r'</.+>', '', document)
        # document = re.sub(r'<.+/>', '', document)
        write_out(filename, document)


def write_out(filename, document):
    encoding = chardet.detect(document)['encoding']
    if encoding is None:
        encoding = 'utf-8'
    document = document.decode(encoding, 'ignore')
    out = open('/home/gavin/PycharmProjects/rcv1-cleaning/data/processed-documents/%s' % filename, 'w')
    out.write("%s" % document.encode('utf-8', 'ignore'))


def open_file(filename):
    with open('/home/gavin/PycharmProjects/rcv1-cleaning/data/documents/%s' % filename) as f:
        return f.read()


def get_filename_list():
    os.chdir("/home/gavin/PycharmProjects/rcv1-cleaning/data/documents")
    files = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            files.append(file)
    return files


if __name__ == '__main__':
    main()