import os

from pyecharts.charts import Bar, Pie
from pymongo import MongoClient
from pyecharts.charts.basic_charts.graph import Graph

from pyecharts import options as opts

nums = []

xaixs = ['3月1日', '3月2日', '3月3日', '3月4日', '3月5日', '3月6日', '3月7日', '3月8日', '3月9日', '3月10日', '3月11日', '3月12日',
         '3月13日', '3月14日', '3月15日', '3月16日', '3月17日', '3月18日', '3月19日', '3月20日 ', '3月21日', '3月22日', '3月23日',
         '3月24日 ', '3月25日', '3月26日', '3月27日', '3月28日', '3月29日', '3月30日', '3月31日']


# 获取每一天的微博数量
def get_nums():
    f = open('resources/datatest.csv', 'r', encoding='utf-8-sig', newline="")

    key = f.readline()

    while key != '':

        lines = int(key.split(' ')[1].replace('\r\n', ''))
        nums.append(lines)
        for i in range(lines):
            f.readline()
        key = f.readline()


def file_exist(path):
    if os.path.exists(path):
        return True
    return False


def get_conn(database, table):
    client = MongoClient(host='127.0.0.1', port=27017)
    db = client.get_database(database)
    conn = db[table]
    return conn


# 得到{id:name}字典
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


# 得到关系字典
def get_relation_dict():
    conn = get_conn('weibo', 'Relationships')
    results = conn.find({}, {'_id': 0, 'fan_id': 1, 'followed_id': 1})
    relationdict = {}
    idnamedict = get_id_name_dict()
    for res in results:
        if idnamedict.get(res['fan_id']) and idnamedict.get(res['followed_id']):
            relationdict.setdefault(idnamedict[res['fan_id']], []).append(idnamedict[res['followed_id']])
        elif idnamedict.get(res['fan_id']):
            relationdict.setdefault(idnamedict[res['fan_id']], []).append(res['followed_id'])
        elif idnamedict.get(res['followed_id']):
            relationdict.setdefault(res['fan_id'], []).append(idnamedict[res['followed_id']])
        else:
            relationdict.setdefault(res['fan_id'], []).append(res['followed_id'])

    # for k, v in relationdict.items():
    #     print(k, '=', v)
    return relationdict


def get_relation_list():
    conn = get_conn('weibo', 'Relationships')
    results = conn.find({}, {'_id': 0, 'fan_id': 1, 'followed_id': 1})
    prelist = []
    idnamedict = get_id_name_dict()
    for res in results:
        if idnamedict.get(res['fan_id']):
            prelist.append(idnamedict[res['fan_id']])
        else:
            prelist.append(res['fan_id'])
        if idnamedict.get(res['followed_id']):
            prelist.append(idnamedict[res['followed_id']])
        else:
            prelist.append(res['followed_id'])
    lstlist = list(set(prelist))
    lstlist.sort(key=prelist.index)

    return lstlist


def get_relation_topo():
    path = 'resources/echarts/topo.html'
    if not file_exist(path):
        print("本地不存在拓扑图，生成中")
        relationdict = get_relation_dict()
        relationlist = get_relation_list()
        nodes = []
        links = []
        count = 0
        for li in relationlist:
            if count <= 200:
                if count == 0:
                    nodes.append({"name": li, "symbolSize": 50})
                else:
                    nodes.append({"name": li, "symbolSize": 20})
                count += 1
        count = 0
        for k, v in relationdict.items():
            for i in v:
                if count <= 200:
                    links.append({"source": k, "target": i})
                    count += 1

        c = (Graph().add("", nodes, links, repulsion=8000, ).set_global_opts(
            title_opts=opts.TitleOpts(title="人物关系拓扑图")))
        c.render(path)
        print('生成成功')


# 获取微博内容数量分布图
def get_count_barchart():
    path = 'resources/echarts/contentscountbar.html'
    if not file_exist(path):
        print('微博内容数量分布柱状图不存在，生成中')
        get_nums()
        bar = Bar()
        bar.add_xaxis(xaixs)

        bar.add_yaxis(series_name='3月份微博内容数量', y_axis=nums)
        bar.set_global_opts(title_opts=opts.TitleOpts(title="", subtitle='三月份'))
        bar.render(path)
        print('生成成功')


def get_count_piechart():
    path = 'resources/echarts/contentscountpie.html'
    if not file_exist(path):
        print('微博内容数量比例图不存在，生成中')
        get_nums()
        c = Pie()
        c.add("", [list(z) for z in zip(xaixs, nums)])
        c.set_global_opts(title_opts=opts.TitleOpts(title="Pie-微博内容数量比例"))
        c.render(path)
        print('生成成功')


def get_all():
    get_relation_topo()
    get_count_barchart()
    get_count_piechart()


if __name__ == '__main__':
    get_all()