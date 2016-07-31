#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
#  @author luosry
#

import requests
import commands
import json
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='',
        passwd='',
        db ='test',
        charset='utf8',
        )
cur = conn.cursor()



import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def getCommentCount(url, songid):
    output = commands.getstatusoutput("phantomjs /Users/luosry/vhost/wymusic/js/comment.js " +url)
    if len(output)>0:
        try:
            j=json.loads(output[1])
            sql = ('insert into music(song,author,comment,songid) values("' +j['name']+'","'+j['author']+'",'+j['c']+',"'+songid+'")')
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print e
            pass

if __name__ == '__main__':
    index=int(sys.argv[1])
    url = 'http://music.163.com/#/song?id='+ str(index)
    getCommentCount(url,str(index))
    conn.close()
