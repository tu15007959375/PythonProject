# encoding: utf-8
import re
import datetime

from pymongo import MongoClient


def time_fix(time_string):
    now_time = datetime.datetime.now()
    if '分钟前' in time_string:
        minutes = re.search(r'^(\d+)分钟', time_string).group(1)
        created_at = now_time - datetime.timedelta(minutes=int(minutes))
        return created_at.strftime('%Y-%m-%d %H:%M')

    if '小时前' in time_string:
        minutes = re.search(r'^(\d+)小时', time_string).group(1)
        created_at = now_time - datetime.timedelta(hours=int(minutes))
        return created_at.strftime('%Y-%m-%d %H:%M')

    if '今天' in time_string:
        return time_string.replace('今天', now_time.strftime('%Y-%m-%d'))

    if '月' in time_string:
        time_string = time_string.replace('月', '-').replace('日', '')
        time_string = str(now_time.year) + '-' + time_string
        return time_string

    return time_string


keyword_re = re.compile('<span class="kt">|</span>|原图|<!-- 是否进行翻译 -->|<span class="cmt">|\[组图共.+张\]')
emoji_re = re.compile('<img alt="|" src="//h5\.sinaimg(.*?)/>')
white_space_re = re.compile('<br />')
div_re = re.compile('</div>|<div>')
image_re = re.compile('<img(.*?)/>')
url_re = re.compile('<a href=(.*?)>|</a>')


def extract_weibo_content(weibo_html):
    s = weibo_html
    if 'class="ctt">' in s:
        s = s.split('class="ctt">', maxsplit=1)[1]
    s = emoji_re.sub('', s)
    s = url_re.sub('', s)
    s = div_re.sub('', s)
    s = image_re.sub('', s)
    if '<span class="ct">' in s:
        s = s.split('<span class="ct">')[0]
    splits = s.split('赞[')
    if len(splits) == 2:
        s = splits[0]
    if len(splits) == 3:
        # origin_text = splits[0]
        # retweet_text = splits[1].split('转发理由:')[1]
        # s = origin_text + '转发理由:' + retweet_text
        return ''
    s = white_space_re.sub(' ', s)
    s = keyword_re.sub('', s)
    s = s.replace('\xa0', '')
    s = s.strip(':')
    s = s.strip()
    return s


def get_mongdb_tweet_id():
    Mongdbidlist = []
    client = MongoClient(host='127.0.0.1', port=27017)
    db = client.get_database("weibo")
    conn = db["Tweet"]
    results = conn.find({}, {'_id': 0, 'user_id': 1})
    for i in results:
        Mongdbidlist.append(i['user_id'])

    return Mongdbidlist


def get_mongdb_relations_all_ids():
    idlist = []
    client = MongoClient(host='127.0.0.1', port=27017)
    db = client.get_database("weibo")
    conn = db["Relationships"]
    results = conn.find({}, {'_id': 0, 'fan_id': 1, 'followed_id': 1})
    for res in results:
        idlist.append(res['fan_id'])
        idlist.append(res['followed_id'])
    idlist = list(set(idlist))
    return idlist
