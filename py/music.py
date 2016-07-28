#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
#  @author luosry
#

import requests
import commands
import json
import os
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='qweqwe',
        db ='test',
        charset='utf8',
        )
cur = conn.cursor()



import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def isOK(url, songid):
    r = requests.get(url)
    a=commands.getstatusoutput("/usr/local/bin/phantomjs /home/luo/pydir/spider/c.js " +url)
    if len(a)>0:
        try:
            j=json.loads(a[1])
            sql = ('insert into music(song,author,comment,songid) values("' +j['name']+'","'+j['author']+'",'+j['c']+',"'+songid+'")')
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            pass

if __name__ == '__main__':
    a=int(sys.argv[1])
    for index in range(a, a+10000000):
        url = 'http://music.163.com/#/song?id='+ str(index)
        isOK(url,str(index))
    conn.close()
