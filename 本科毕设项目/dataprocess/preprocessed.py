import re
import datetime
from pymongo import MongoClient
import csv
import sys
from dateutil.parser import *


def get_conn(database, table):
    client = MongoClient(host='127.0.0.1', port=27017)
    db = client.get_database(database)
    conn = db[table]
    return conn


# 将数据库数据进行数据清洗存到datatest.csv文件中
def dict_to_csv():
    count = 0

    infodict = get_infomationdict_bytime()
    namelist = csv_to_list('resources/namelist.csv')

    for key, values in infodict.items():
        dellist = []
        # values为[id!@#content!@#url][][][]...
        for i in range(len(values)):
            # valuelist [id][content][url]
            valuelist = str(values[i]).split('!@$')
            x = re.sub(r"<.*>", "", valuelist[1])
            x = re.sub(r"【.*】", "", x)
            x = re.sub(r"#.*#", "", x)
            x = x.strip()
            print(str(count) + ":" + x)
            endpos = sys.maxsize
            if x.rfind(' ') != -1:
                endpos = x.rfind(' ')
            if x.rfind('@') != -1:
                endpos = min(endpos, x.rfind('@'))
            if x.rfind('的') != -1:
                endpos = min(endpos, x.rfind('的'))
            x = x[:endpos]
            x = re.sub(r"\d{4}年\d{1,2}月\d{1,2}日", '', x)
            x = re.sub(r"\d{4}年\d{1,2}月", '', x)
            x = re.sub(r"\d{1,2}月\d{1,2}日", '', x)
            x = re.sub('[^\u4e00-\u9fa5]+', '', x)
            x = x.replace('re.sub('', '', x) ', '')  # 去除‘当地时间’
            x = x.replace('\u54c8', '')  # 去除‘哈’
            x = x.replace('\u56fe\u7247\u6765\u6e90', '')  # 去除‘图片来源’
            x = x.replace('\u5fae\u535a\u89c6\u9891', '')  # 去除‘微博视频’
            x = x.replace('\u8f6c\u53d1\u7406\u7531', '')  # 去除‘转发理由’
            x = x.replace('\u6233\u89c6\u9891', '')  # 去除‘戳视频’
            x = x.replace('\u6233\u94fe\u63a5', '')  # 去除‘戳链接’

            for j in range(len(namelist)):
                dele = str(namelist[j][0]) + '的'
                dele2 = str(namelist[j][0])
                if dele in x or dele2 in x:
                    x = x.replace(dele, '')
                    x = x.replace(dele2, '')
                    break
            if x != "" and 5 <= len(x) <= 200:
                count += 1
                prestr = str(values[i]).split('!@$')[1]
                values[i] = values[i].replace(prestr, x)
            else:
                dellist.append(i)
        infodict[key] = [k for num, k in enumerate(values) if num not in dellist]

    f = open('resources/datatest.csv', 'a', encoding='utf-8-sig', newline="")
    csv_write = csv.writer(f)

    for key, values in infodict.items():
        csv_write.writerow([key + ' ' + str(len(values))])
        for i in range(len(values)):
            csv_write.writerow([values[i]])


def get_namelist():
    conn = get_conn('weibo', 'Users')
    results = conn.find({}, {'_id': 0, 'nick_name': 1})
    namelist = []
    for res in results:
        if len(res) != 0 and res['nick_name'] != '':
            x = re.sub(r"<.*>", "", res['nick_name'])
            x = re.sub(r"【.*】", "", x)
            x = re.sub(r"#.*#", "", x)
            x = re.sub('[^\u4e00-\u9fa5]+', '', x)
            if x != '':
                namelist.append(x)
    return namelist


def csv_to_list(file_name):
    f = open(file_name, 'r', encoding='utf-8-sig', newline="")
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    return final_list


def get_infomationdict_bytime():
    conn = get_conn('weibo', 'Tweet')
    # starttime = parse(starttime)
    # endtime = parse(endtime)
    results = conn.aggregate([{"$project": {'_id': 0, 'content': 1, 'created_at': 1, 'user_id': 1, 'weibo_url': 1}},
                              ])
    infodict = {}
    for res in results:
        # dict形式为{'time':[id!@$context!@$url],'time':[id!@$context!@$url]}
        if res['content'] != '':
            infodict.setdefault((str(res['created_at'])).split(' ')[0], []).append(
                res['user_id'] + '!@$' + res['content'] + '!@$' + res['weibo_url'])
    # 按照dict的键即时间排序返回
    infodict = dict(sorted(infodict.items(), key=lambda k: k[0]))
    return infodict


if __name__ == '__main__':
    # namelist = get_namelist()
    # f = open('resources/namelist.csv.csv', 'w', encoding='utf-8-sig', newline="")
    # csv_write = csv.writer(f)
    # for li in namelist:
    #     csv_write.writerow([li])
    dict_to_csv()
    pass
