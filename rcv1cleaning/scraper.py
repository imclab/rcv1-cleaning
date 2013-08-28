#!/usr/bin/env python
"""

"""
import os
from urllib import urlopen
import hashlib
import chardet
import requests
from requests.exceptions import HTTPError, ConnectionError
from requests.packages.urllib3.exceptions import DecodeError

def main():
    hashesList = []
    files = get_url_list_files()
    for file in files:
        print '** Starting file', file
        with open('/home/data/urls/%s' % file) as f:
            urls = f.read().splitlines()
            for url in urls:
                print '**** Starting URL', url, 'in file', file
                try:
                    r = requests.get(url)
                    r.raise_for_status()
                except HTTPError:
                    print 'Could not download resource', url
                except ConnectionError:
                    print 'Connection error for', url
                except DecodeError:
                    print 'Decode error for', url
                except Exception:
                    print 'An exception occured on', url
                else:
                    print r.url, 'downloaded successfully'
                    hash = writeOut(url, r.text)
                    hashesList.append((url, hash))

    out = open('/home/data/pages/urls-hashes.txt', 'w')
    for hash in hashesList:
        out.write("%s\n" % hash)
    out.close()


def writeOut(url, document):
    encoding = chardet.detect(document)['encoding']
    if encoding is None:
        encoding = 'utf-8'
    hash = hashlib.md5(url).hexdigest()
    out = open('/home/data/pages/page-%s.txt' % hash, 'w')
    try:
        # document = document.decode(encoding, 'replace')
        out.write(document.encode('utf-8', 'replace'))
        out.close()
    except UnicodeDecodeError:
        print 'Could not decode document'
    except UnicodeEncodeError:
        print 'Could not encode document'
    return hash


def get_url_list_files():
    os.chdir("/home/data/urls")
    files = []
    for file in os.listdir("."):
        if file.endswith(".txt"):
            files.append(file)
    return files


if __name__ == '__main__':
    main()