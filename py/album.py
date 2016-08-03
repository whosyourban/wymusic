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

def getAlbum(artistId,url):
    output = commands.getstatusoutput("phantomjs /Users/luosry/vhost/wymusic/js/album.js '%s'" % url)
    if len(output)>0:
        try:
            result = output[1].split('\n')
            if result[0]=='':
                return False
            for data in result:
                print data
                j=json.loads(data)
                sql = 'insert into album(artist_id, album_id, name, create_at) values("%s","%s","%s","%s")' % (artistId, j['id'], j['name'],j['date'])
                cur.execute(sql)
                conn.commit()
        except Exception as e:
            print e
            pass
        return True



if __name__ == '__main__':
    sql = 'select artist_id from singer where id>= 26540 '
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print row
        artistId = row[0]
        print artistId
        for i in range(0, 3600, 12):
            url = 'http://music.163.com/#/artist/album?id=%s&limit=12&offset=%d' % (artistId, i)
            ok = getAlbum(artistId, url)
            if not ok:
                break

    conn.close()
