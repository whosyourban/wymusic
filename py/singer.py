#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
#  @author luosry
#  根据分类获取所有歌手id,
#  详细参考 http://music.163.com/#/discover/artist

import commands
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


baseurl = 'http://music.163.com/#'

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

jspath = '/Users/luosry/vhost/wymusic/js/'
jsconfig = jspath + 'config.json'


def get_links(url, jsfile):
    url = url.encode()
    # url一定要加单引号---原因暂时未知，估计是shell的处理有问题。在py脚本中调用的话怎么请求也是返回热门歌手页面的数据
    cmd = "phantomjs --config=%s %s '%s'" % (jsconfig ,jspath+jsfile ,url)
    output = commands.getstatusoutput(cmd)
    if len(output)>0:
        try:
            result = output[1].split('\n')
        except Exception as e:
            print e
    else:
        pass
    return result


def save_singers(singers):
    for singer in singers:
        try:
            # TDOO 这样粗暴地拼接sql遇到双引号会有问题
            tmp = singer.replace('"',"").split("|||")
            sql = 'insert into singer(author,artist_id) values("%s",%d)' % (tmp[0].replace('的音乐',''), int(tmp[1].replace('/artist?id=','')))
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print e

if __name__ == '__main__':
    # 1000华 2000欧 7000日 4000韩 , 1男歌手，2女歌手，3组合/乐队
    urls = [
        'http://music.163.com/#/discover/artist/cat?id=1001',
        'http://music.163.com/#/discover/artist/cat?id=1002',
        'http://music.163.com/#/discover/artist/cat?id=1003',
        'http://music.163.com/#/discover/artist/cat?id=2001',
        'http://music.163.com/#/discover/artist/cat?id=2002',
        'http://music.163.com/#/discover/artist/cat?id=2003',
        'http://music.163.com/#/discover/artist/cat?id=7001',
        'http://music.163.com/#/discover/artist/cat?id=7002',
        'http://music.163.com/#/discover/artist/cat?id=7003',
        'http://music.163.com/#/discover/artist/cat?id=4001',
        'http://music.163.com/#/discover/artist/cat?id=4002',
        'http://music.163.com/#/discover/artist/cat?id=4003',
    ]
    # 歌手按 A-Z 分类, 其实就是在url后面加initial参数(65~91),0 代表未分类,-1代表热门歌手
    categorys =range(65, 91)
    categorys.insert(0,-1)
    categorys.append(0)

    for url in urls:
        for c in categorys:
            singers = get_links( url+'&initial='+str(c) , 'singer.js')
            save_singers(singers)
    conn.close()
