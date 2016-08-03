#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
#  @author luosry
#

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

# TODO threads
def getCommentCount(url, songid):
    output = commands.getstatusoutput("phantomjs /Users/luosry/vhost/wymusic/js/comment.js " +url)
    if len(output)>0:
        try:
            j=json.loads(output[1])
            sql = ('insert into music(song,author,comment,songid) values("' +j['name']+'","'+j['author']+'",'+j['c']+',"'+songid+'")')
            print sql
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print e
            pass

def getalbumSongs(url):
    output = commands.getstatusoutput("phantomjs /Users/luosry/vhost/wymusic/js/songs.js " +url)
    if len(output)>0:
        return output[1].split('\n')
    else:
        pass
    return []



if __name__ == '__main__':
    index = 75
    while True:
        sql = 'select album_id from album limit %d,10' % index
        index = index + 10
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows)<=0:
            break
        for row in rows:
            album_id = row[0]
            print album_id
            album_url = 'http://music.163.com/#/album?id='+album_id
            song_ids = getalbumSongs(album_url)
            print song_ids
            for song_id in song_ids:
                url = 'http://music.163.com/#/song?id='+ song_id
                getCommentCount(url,song_id)
    conn.close()
