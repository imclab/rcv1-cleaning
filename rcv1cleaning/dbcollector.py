#!/usr/bin/env python
"""

"""
from time import sleep
import MySQLdb


def load_dom_ids():
    with open('/home/gavin/dev/rcv1/mvp2/domain_ids.csv') as f:
        dom_ids = f.readlines()
    return dom_ids


def execute_query(dom_id):
    user = 'readonly'
    password = 'Integration1'
    db = 'picad_parser'
    host = 'ec2-50-16-171-247.compute-1.amazonaws.com'
    conn = MySQLdb.Connection(user=user, passwd=password, db=db, host=host)
    cursor = conn.cursor()
    cursor.execute("""SELECT id, domain_id, content from `picad_parser`.`pub_articles` WHERE domain_id=%s LIMIT 500""" % dom_id)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == '__main__':
    dom_ids = load_dom_ids()
    for dom_id in dom_ids:
        outFile = open('/home/gavin/dev/rcv1/mvp2/%s.txt' % dom_id, 'w')
        print 'executing query with dom_id', dom_id
        results = execute_query(dom_id)
        for result in results:
            print>>outFile, result
        print 'sleeping'
        sleep(60*1.5)
