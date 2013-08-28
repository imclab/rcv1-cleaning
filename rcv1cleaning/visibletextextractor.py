#!/usr/bin/env python
"""

"""
import os
import re
from BeautifulSoup import BeautifulSoup
import chardet


def main():
    filenames = get_filename_list()
    for filename in filenames:
        print '** Starting file', filename
        html = open_file(filename)
        visible_text = extract_visible_text(html)
        write_out(filename, visible_text)


def open_file(filename):
    with open('/home/gavin/PycharmProjects/rcv1-cleaning/data/pages/%s' % filename) as f:
        return f.read()


def write_out(filename, visible_text):
    encoding = chardet.detect(visible_text)['encoding']
    if encoding is None:
        encoding = 'utf-8'
    # visible_text = visible_text.decode(encoding, 'ignore')
    out = open('/home/gavin/PycharmProjects/rcv1-cleaning/data/documents/%s.txt' % filename, 'w')
    out.write("%s" % visible_text.encode('utf-8', 'ignore'))


def extract_visible_text(html):
    soup = BeautifulSoup(html)
    texts = soup.findAll(text=True)

    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True

    visible_texts = filter(visible, texts)
    visible_text = ' '.join(visible_texts)
    visible_text = visible_text.replace('\n', '')
    visible_text = visible_text.replace('\r', '')
    visible_text = visible_text.replace('\t', '')
    visible_text = visible_text.replace('&nbsp;', '')
    visible_text = visible_text.replace('    ', ' ')
    visible_text = visible_text.replace('   ', ' ')
    visible_text = visible_text.replace('  ', ' ')
    print repr(visible_text)
    return visible_text


def get_filename_list():
    os.chdir("/home/gavin/PycharmProjects/rcv1-cleaning/data/pages")
    files = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            files.append(file)
    return files


if __name__ == '__main__':
    main()