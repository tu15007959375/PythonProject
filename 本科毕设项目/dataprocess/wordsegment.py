import csv
import os
from pprint import pprint
import gensim
import jieba
import pandas as pd
import pkuseg
from collections import Counter
import pprint
import pyLDAvis.gensim_models
import thulac
from gensim import corpora
from gensim.models import CoherenceModel

from snownlp import SnowNLP
import time


# 转换成可以计算词频的格式
def get_newlist(infodict, starttime, endtime):
    new_text = []
    # 得到限定时间的列表
    datalist = get_datalist(infodict, starttime, endtime)
    stopwords = get_stopstr()
    for w in datalist:
        for v in w:
            if v not in stopwords:
                new_text.append(v)
    return new_text


# 获得gensimlda列表
def get_gensim_ldalist(infodict, starttime='2022-03-01', endtime='2022-03-31'):
    ldalist = []
    i = 0
    for key, values in infodict.items():
        if compare_time(key, starttime) and compare_time(endtime, key):
            for value in values:
                ldalist.append(value.split('!@$')[1].split(' '))
                i += 1
    stoplist = get_stoplist()
    for i in range(len(ldalist)):
        for j in range(len(ldalist[i]) - 1, -1, -1):
            if ldalist[i][j] in stoplist:
                ldalist[i].pop(j)

    return ldalist


# 获得sklearngensimlda列表
def getsklearnldalist(infodict, starttime='2022-03-01', endtime='2022-03-31'):
    ldalist = []
    for key, values in infodict.items():
        if compare_time(key, starttime) and compare_time(endtime, key):
            for value in values:
                ldalist.append(value.split('!@$')[1])
    stoplist = get_stoplist()
    for i in range(len(ldalist)):
        x = ldalist[i].split(' ')
        for j in range(len(x) - 1, -1, -1):
            if x[j] in stoplist:
                x.pop(j)
        ldalist[i] = ' '.join(x)

    return ldalist


# 得到分词后微博内容的列表
def get_datalist(infodict, starttime, endtime):
    datalist = []
    for key, values in infodict.items():
        # 限定时间
        if compare_time(key, starttime) and compare_time(endtime, key):
            for value in values:
                datalist.extend([value.split('!@$')[1].split(' ')])
    return datalist


# 获取停用词字符串
def get_stopstr():
    with open("resources/stopword.txt", encoding="utf-8-sig") as f:
        return f.read()


# 获取停用词列表
def get_stoplist():
    return [line.strip() for line in open('resources/stopword.txt', encoding='utf-8-sig').readlines()]


# 时间比对方法
def compare_time(time1, time2):
    s_time = time.mktime(time.strptime(time1, '%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2, '%Y-%m-%d'))
    if (int(s_time) - int(e_time)) >= 0:
        return True
    return False


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


def dic_to_csv(infodict, method):
    f = open('resources/datasegfile/' + method + 'seg.csv', 'w', encoding='utf-8-sig', newline="")
    csv_write = csv.writer(f)

    for key, values in infodict.items():
        csv_write.writerow([key + ' ' + str(len(values))])
        for i in range(len(values)):
            csv_write.writerow([values[i]])


# 根据开始时间和结束时间对count文件对应日期的词频进行抽取
def get_countdict_from_file(path, starttime, endtime):
    countdict = {}
    flag = 0
    with open(path, 'r', encoding='utf-8-sig', newline="") as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            # 从文件读取，判断开始时间和结束时间是否符合
            if flag == 1 and count < 30:
                countdict[row[0].split(' ')[0]] = row[0].split(' ')[1].replace('\r\n', '')
                count += 1
            if (i + 1) % 31 == 1 and starttime == row[0].split(' ')[0] and endtime == row[0].split(' ')[1].replace(
                    '\r\n', ''):
                flag = 1
                count = 0

    return countdict


def get_snowlp(starttime, endtime):
    conuntdict = {}
    path = 'resources/countfile/snowlpcount.csv'
    # 判断词频文件是否存在以及文件中是否存在该日期
    if os.path.exists(path):
        conuntdict = get_countdict_from_file(path, starttime, endtime)
    if conuntdict:
        return conuntdict
    print("生成词频文件中。。。。。")
    path = 'resources/datasegfile/snowlpseg.csv'
    # 判断分词文件是否存在
    if not os.path.exists(path):
        infodict = get_infodict_from_csv()
        for key, values in infodict.items():
            # values为[id!@#content!@#url][][][]...
            for i in range(len(values)):
                prestr = str(values[i]).split('!@$')[1]
                snowlpastr = ''
                j = 0
                for li in SnowNLP(prestr).words:
                    if j == 0:
                        snowlpastr = snowlpastr + li
                    else:
                        snowlpastr = snowlpastr + ' ' + li
                    j = 1

                values[i] = values[i].replace(prestr, snowlpastr)

        dic_to_csv(infodict, 'snowlp')
    else:
        infodict = get_infodict_from_csv(path)
    new_text = get_newlist(infodict, starttime, endtime)
    return writer_counter_to_csv(new_text, 'snowlp', starttime, endtime)


def get_thulac(starttime, endtime):
    conuntdict = {}
    path = 'resources/countfile/thulaccount.csv'
    # 判断词频文件是否存在以及文件中是否存在该日期
    if os.path.exists(path):
        conuntdict = get_countdict_from_file(path, starttime, endtime)
    if conuntdict:
        return conuntdict
    else:
        print("生成词频文件中。。。。。")
        path = 'resources/datasegfile/thulacseg.csv'
        # 判断分词文件是否存在
        if not os.path.exists(path):
            thu = thulac.thulac(user_dict='resources/mydict.txt', seg_only=True)
            infodict = get_infodict_from_csv()
            for key, values in infodict.items():
                # values为[id!@#content!@#url][][][]...
                for i in range(len(values)):
                    prestr = str(values[i]).split('!@$')[1]
                    segstr = ''
                    j = 0
                    # [['虞书欣', ''], ['被', ''], ['选中', ''], ['这', ''], ['段', ''], ['爆炸', ''], ['可爱', ''], ['恭喜欣子', ''], ['追星', ''], ['成功', '']]
                    for li in thu.cut(prestr):
                        if j == 0:
                            segstr = segstr + str(li[0])
                        else:
                            segstr = segstr + ' ' + str(li[0])
                        j = 1
                    values[i] = values[i].replace(prestr, segstr)
            # 保存全部分词结果到csv
            dic_to_csv(infodict, 'thulac')
        else:
            infodict = get_infodict_from_csv(path)
        # 下面计算词频，限定时间段
        new_text = get_newlist(infodict, starttime, endtime)
        return writer_counter_to_csv(new_text, 'thulac', starttime, endtime)


def get_pkuseg(starttime, endtime):
    conuntdict = {}
    path = 'resources/countfile/pkusegcount.csv'
    # 判断词频文件是否存在以及文件中是否存在该日期
    if os.path.exists(path):
        conuntdict = get_countdict_from_file(path, starttime, endtime)
    if conuntdict:
        return conuntdict
    else:
        print("生成词频文件中。。。。。")
        path = 'resources/datasegfile/pkusegseg.csv'
        # 判断分词文件是否存在
        if not os.path.exists(path):
            seg = pkuseg.pkuseg(model_name="news", user_dict='resources/mydict.txt')  # 以新闻加载模型
            infodict = get_infodict_from_csv()

            for key, values in infodict.items():
                # values为[id!@#content!@#url][][][]...
                for i in range(len(values)):
                    prestr = str(values[i]).split('!@$')[1]
                    segstr = ''
                    j = 0
                    for li in seg.cut(prestr):
                        if j == 0:
                            segstr = segstr + li
                        else:
                            segstr = segstr + ' ' + li
                        j = 1

                    values[i] = values[i].replace(prestr, segstr)

            dic_to_csv(infodict, 'pkuseg')
        else:
            infodict = get_infodict_from_csv(path)
        # 下面计算词频，限定时间段
        new_text = get_newlist(infodict, starttime, endtime)
        return writer_counter_to_csv(new_text, 'pkuseg', starttime, endtime)


def get_jieba(starttime, endtime):
    conuntdict = {}
    path = 'resources/countfile/jiebacount.csv'
    # 判断词频文件是否存在以及文件中是否存在该日期
    if os.path.exists(path):
        conuntdict = get_countdict_from_file(path, starttime, endtime)
    if conuntdict:
        return conuntdict
    else:
        print("生成词频文件中。。。。。")
        path = 'resources/datasegfile/jiebaseg.csv'
        # 判断分词文件是否存在
        if not os.path.exists(path):
            infodict = get_infodict_from_csv()
            jieba.load_userdict('resources/mydict.txt')
            for key, values in infodict.items():
                # values为[id!@#content!@#url][][][]...
                for i in range(len(values)):
                    prestr = str(values[i]).split('!@$')[1]
                    jiebastr = ''
                    j = 0
                    for li in jieba.lcut(prestr):
                        if j == 0:
                            jiebastr = jiebastr + li
                        else:
                            jiebastr = jiebastr + ' ' + li
                        j = 1
                    values[i] = values[i].replace(prestr, jiebastr)
            dic_to_csv(infodict, 'jieba')
        else:
            infodict = get_infodict_from_csv(path)
        new_text = get_newlist(infodict, starttime, endtime)
        return writer_counter_to_csv(new_text, 'jieba', starttime, endtime)


def get_gensim_lda_tfidf(method):
    path = 'resources/lda/' + method + 'ldatfidflda2022-03-01_2022-03-31.html'
    if not os.path.exists(path):
        infodict = get_infodict_from_csv('resources/datasegfile/' + method + 'seg.csv')
        ldalist = get_gensim_ldalist(infodict)
        # 创建字典和词袋
        id2word = corpora.Dictionary(ldalist)
        # 将字典转换为词袋,为文档中的每一个单词创建唯一的ID
        corpus = [id2word.doc2bow(sentence) for sentence in ldalist]
        tfidf = gensim.models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        # 建立LDA模型
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf,
                                                    id2word=id2word,
                                                    num_topics=4,
                                                    # random_state=100,
                                                    # update_every=1,
                                                    # chunksize=100,
                                                    # passes=10,
                                                    # alpha='auto',
                                                    # per_word_topics=True
                                                    )
        coherencemodel = CoherenceModel(model=lda_model, texts=ldalist, dictionary=id2word, coherence='c_v')
        print(coherencemodel.get_coherence())

        d = pyLDAvis.gensim_models.prepare(lda_model, corpus_tfidf, id2word)
        pyLDAvis.save_html(d, path)  # 将结果保存为该html文件


def get_gensim_lda_mallet(method, num_topic):
    path = 'resources/lda/' + method + 'mallet' + str(num_topic)
    if not os.path.exists(path):
        infodict = get_infodict_from_csv('resources/datasegfile/' + method + 'seg.csv')
        ldalist = get_gensim_ldalist(infodict)
        # 创建字典和词袋
        id2word = corpora.Dictionary(ldalist)
        # 将字典转换为词袋,为文档中的每一个单词创建唯一的ID
        corpus = [id2word.doc2bow(sentence) for sentence in ldalist]
        os.environ['MALLET_HOME'] = 'D:/SoftWare/mallet-2.0.8/'
        mallet_path = 'D:/SoftWare/mallet-2.0.8/bin/mallet'  # update this path
        ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topic, id2word=id2word)
        coherencemodel = CoherenceModel(model=ldamallet, texts=ldalist, dictionary=id2word, coherence='c_v')
        cohernce = round(coherencemodel.get_coherence(), 3)
        path += '_' + str(cohernce) + '.html'
        model = gensim.models.wrappers.ldamallet.malletmodel2ldamodel(mallet_model=ldamallet)
        d = pyLDAvis.gensim_models.prepare(model, corpus, id2word)
        pyLDAvis.save_html(d, path)  # 将结果保存为该html文件


def get_gensim_lda(method, num_topics):
    path = 'resources/lda/' + method + 'lda_' + str(num_topics)
    infodict = get_infodict_from_csv('resources/datasegfile/' + method + 'seg.csv')
    ldalist = get_gensim_ldalist(infodict)
    # 创建字典和词袋
    id2word = corpora.Dictionary(ldalist)
    # 将字典转换为词袋,为文档中的每一个单词创建唯一的ID
    corpus = [id2word.doc2bow(sentence) for sentence in ldalist]

    # 建立LDA模型
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=num_topics,
                                                # random_state=100,
                                                # update_every=1,
                                                # chunksize=100,
                                                # passes=10,
                                                # alpha='auto',
                                                # per_word_topics=True
                                                )
    coherencemodel = CoherenceModel(model=lda_model, texts=ldalist, dictionary=id2word, coherence='c_v')
    cohernce = round(coherencemodel.get_coherence(), 3)
    print(method + str(num_topics) + ':' + str(cohernce))
    path += '_' + str(cohernce) + '.html'
    d = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(d, path)  # 将结果保存为该html文件


# 统计词频并且写入对应的文件中
def writer_counter_to_csv(new_text, method, starttime, endtime):
    counter = Counter(new_text)
    pprint.pprint(counter.most_common(30))
    countdict = {}
    for data in counter.most_common(30):
        countdict[data[0]] = data[1]

    f = open('resources/countfile/' + method + 'count.csv', 'a', encoding='utf-8-sig', newline="")
    csv_write = csv.writer(f)
    csv_write.writerow([starttime + ' ' + endtime])
    for key, values in countdict.items():
        csv_write.writerow([key + ' ' + str(values)])
    return countdict


def get_all_segment(starttime, endtime):
    get_pkuseg(starttime, endtime)
    get_jieba(starttime, endtime)
    get_thulac(starttime, endtime)
    get_snowlp(starttime, endtime)


def get_all_lda(num_topics):
    get_gensim_lda('pkuseg', num_topics)
    get_gensim_lda('jieba', num_topics)
    get_gensim_lda('thulac', num_topics)
    get_gensim_lda('snowlp', num_topics)


def get_all():
    get_all_segment('2022-03-01', '2022-03-07')


if __name__ == '__main__':
    get_pkuseg('2022-03-01', '2022-03-07')
    # for i in range(7, 11):
    #     get_gensim_lda_mallet('jieba', i)
    # for i in range(9, 13):
    #     get_gensim_lda_mallet('pkuseg', i)
    # for i in range(7, 13):
    #     get_gensim_lda_mallet('snowlp', i)
    # for i in range(10, 15):
    #     get_gensim_lda_mallet('thulac', i)
        # get_gensim_lda('jieba', num)
        # get_gensim_lda('pkuseg', num)
        # get_gensim_lda('snowlp', num)
        # get_gensim_lda('thulac', num)
