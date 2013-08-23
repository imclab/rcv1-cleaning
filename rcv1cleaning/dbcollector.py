#!/usr/bin/env python
"""

"""
from time import sleep
import MySQLdb


def load_dom_ids():
    with open('/home/ghackeling/nsp/rcv1-cleaning/data/domain_ids.csv') as f:
        dom_ids = f.readlines()
    return dom_ids


def execute_query(dom_id):
    user = ''
    password = ''
    db = ''
    host = 'e'
    conn = MySQLdb.Connection(user=user, passwd=password, db=db, host=host)
    cursor = conn.cursor()
    cursor.execute("""SELECT id, domain_id, content from `picad_parser`.`pub_articles` WHERE domain_id=%s LIMIT 500""" % dom_id)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == '__main__':
    dom_ids = load_dom_ids()
    for dom_id in dom_ids:
        print 'executing query with dom_id', dom_id
        results = execute_query(dom_id)
        for result in results:
            print result
        print 'sleeping'
        sleep(60*3)
