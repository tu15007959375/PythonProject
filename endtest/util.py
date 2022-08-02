import csv
import datetime
import os

import pymongo


def get_conn(dbname='weibo', conn='Tweet'):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    conn = mydb[conn]
    return conn


def get_id_name_dict():
    conn = get_conn('weibo', 'Users')
    results = conn.find({}, {'_id': 1, 'nick_name': 1})
    idnamedict = {}

    for res in results:
        if 'nick_name' in res.keys():
            idnamedict[res['_id']] = res['nick_name']
    # for k, v in idnamedict.items():
    #     print(k, '=', v)
    return idnamedict


def get_userlist():
    conn = get_conn('weibo', 'Admin')
    results = conn.find({}, {'_id': 1, 'tag': 1, 'nick': 1, 'sex': 1})
    userlist = []

    for res in results:
        userlist.append(str(res['_id']) + '!@' + str(res['tag']) + '!@' + str(res['nick']) + '!@' + str(res['sex']))
    return userlist


def get_infodict_from_csv(file_name='resources/datatest.csv'):
    f = open(file_name, 'r', encoding='utf-8-sig', newline="")
    infodict = {}
    key = f.readline()
    while key != '':
        lines = int(key.split(' ')[1].replace('\r\n', ''))
        for i in range(lines):
            infodict.setdefault(key.split(' ')[0], []).append(f.readline().replace('\r\n', ''))
        key = f.readline()
    return infodict


def read_csv_to_list(path):
    f = open(path, 'r', encoding='utf-8-sig', newline="")
    csvreader = csv.reader(f)
    prelist = list(csvreader)
    finlist = []
    for li in prelist:
        if len(li) != 0 and li is not None and li != '':
            finlist.append(li[0])
    return finlist


def save_history(user='', method='', starttime='', endtime='', caltype=''):
    f = open('resources/history/history.csv', 'a', encoding='utf-8-sig', newline="")

    csv_write = csv.writer(f)
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if method == '':
        csv_write.writerow(
            [curr_time + '：' + '用户' + str(user) + '进行了操作：' + caltype])
        return
    csv_write.writerow(
        [curr_time + '：' + '用户' + str(
            user) + '使用' + method + '方法，在时间段' + starttime + '到时间段' + endtime + '进行了操作：' + caltype])


def write_list_to_csv(datalist, path):
    f = open(path, 'a+', encoding='utf-8-sig', newline="")
    writer = csv.writer(f)

    for li in datalist:
        writer.writerow([li])


def file_exist(path):
    if os.path.exists(path):
        return True
    return False
