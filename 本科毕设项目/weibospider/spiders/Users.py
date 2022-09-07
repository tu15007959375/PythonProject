#!/usr/bin/env python
# encoding: utf-8

import re
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from items import RelationshipItem, UserItem, TweetItem
import time
import datetime
from lxml import etree
from urllib.parse import unquote

from spiders.utils import extract_weibo_content, time_fix, get_mongdb_tweet_id, get_mongdb_relations_all_ids


def init_url_by_user_id_and_date(users_id):
    # crawl specific users' tweets in a specific date
    # === change the following config ===
    start_date = datetime.datetime.strptime("2022-3-1", '%Y-%m-%d')
    end_date = datetime.datetime.strptime("2022-3-31", '%Y-%m-%d')
    # === change the above config ===
    time_spread = datetime.timedelta(days=20)
    url_format = "https://weibo.cn/{}/profile?hasori=0&haspic=0&starttime={}&endtime={}&advancedfilter=1&page=1"
    urls = []
    while start_date < end_date:
        for user_id in users_id:
            start_date_string = start_date.strftime("%Y%m%d")
            tmp_end_date = start_date + time_spread
            if tmp_end_date >= end_date:
                tmp_end_date = end_date
            end_date_string = tmp_end_date.strftime("%Y%m%d")
            urls.append(url_format.format(user_id, start_date_string, end_date_string))
        start_date = start_date + time_spread
    return urls


class Users(Spider):
    name = "UserSpider"
    base_url = "https://weibo.cn"
    Mongdbidlist = []
    nowuids = []
    relationsids = []

    def start_requests(self):
        self.Mongdbidlist = get_mongdb_tweet_id()  # 取出数据库的id防止重复
        self.relationsids = get_mongdb_relations_all_ids()
        uid = '2803301701'
        if len(self.Mongdbidlist) != 0:
            uid = self.Mongdbidlist.pop()
        user_ids = [uid]

        urls = [f"{self.base_url}/{user_id}/follow?page=1" for user_id in user_ids]
        urls2 = [f'{self.base_url}/{user_id}/info' for user_id in user_ids]

        urls3 = init_url_by_user_id_and_date(user_ids)
        for url, url2, url3 in zip(urls, urls2, urls3):
            yield Request(url2, callback=self.parseuser, priority=3)
            yield Request(url3, callback=self.parse_tweet, priority=2)
            yield Request(url, callback=self.parse_follow, priority=1)

    def parse_follow(self, response):
        if response.url.endswith('page=1'):
            all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
            if all_page:
                all_page = all_page.group(1)
                all_page = int(all_page)
                # for page_num in range(2, all_page + 1):
                #     page_url = response.url.replace('page=1', 'page={}'.format(page_num))
                #     yield Request(page_url, self.parse_follow, dont_filter=True, meta=response.meta)
                # 爬取前两页
                if all_page >= 2:
                    page_url = response.url.replace('page=1', 'page={}'.format(2))
                    yield Request(page_url, self.parse_follow, dont_filter=True, meta=response.meta)

        selector = Selector(response)
        urls = selector.xpath('//a[text()="关注他" or text()="关注她" or text()="取消关注"]/@href').extract()
        uids = re.findall('uid=(\d+)', ";".join(urls), re.S)
        ID = re.findall('(\d+)/follow', response.url)[0]
        self.nowuids = list(set(uids) - set(self.Mongdbidlist))
        self.Mongdbidlist = self.nowuids + self.Mongdbidlist
        relist = list(set(self.nowuids) - set(self.relationsids))

        self.relationsids = self.relationsids + relist
        for uid in relist:
            relationships_item = RelationshipItem()
            relationships_item['crawl_time'] = int(time.time())
            relationships_item["fan_id"] = ID
            relationships_item["followed_id"] = uid
            yield relationships_item

        uids = self.nowuids
        for uid in uids:
            yield Request(f'{self.base_url}/{uid}/info', callback=self.parseuser, priority=3)
        urls3 = init_url_by_user_id_and_date(uids)
        for url in urls3:
            yield Request(url, callback=self.parse_tweet, priority=2)
        for i in range(len(uids)):
            yield Request(f"{self.base_url}/{uids[len(uids) - i - 1]}/follow?page=1", callback=self.parse_follow,
                          priority=1)

    def parseuser(self, response):
        user_item = UserItem()
        user_item['crawl_time'] = int(time.time())
        selector = Selector(response)
        user_item['_id'] = re.findall('(\d+)/info', response.url)[0]
        user_info_text = ";".join(selector.xpath('body/div[@class="c"]//text()').extract())
        nick_name = re.findall('昵称;?:?(.*?);', user_info_text)
        gender = re.findall('性别;?:?(.*?);', user_info_text)
        place = re.findall('地区;?:?(.*?);', user_info_text)
        brief_introduction = re.findall('简介;?:?(.*?);', user_info_text)
        birthday = re.findall('生日;?:?(.*?);', user_info_text)
        sex_orientation = re.findall('性取向;?:?(.*?);', user_info_text)
        sentiment = re.findall('感情状况;?:?(.*?);', user_info_text)
        vip_level = re.findall('会员等级;?:?(.*?);', user_info_text)
        authentication = re.findall('认证;?:?(.*?);', user_info_text)
        labels = re.findall('标签;?:?(.*?)更多>>', user_info_text)
        if nick_name and nick_name[0]:
            user_item["nick_name"] = nick_name[0].replace(u"\xa0", "")
        if gender and gender[0]:
            user_item["gender"] = gender[0].replace(u"\xa0", "")
        if place and place[0]:
            place = place[0].replace(u"\xa0", "").split(" ")
            user_item["province"] = place[0]
            if len(place) > 1:
                user_item["city"] = place[1]
        if brief_introduction and brief_introduction[0]:
            user_item["brief_introduction"] = brief_introduction[0].replace(u"\xa0", "")
        if birthday and birthday[0]:
            user_item['birthday'] = birthday[0]
        if sex_orientation and sex_orientation[0]:
            if sex_orientation[0].replace(u"\xa0", "") == gender[0]:
                user_item["sex_orientation"] = "同性恋"
            else:
                user_item["sex_orientation"] = "异性恋"
        if sentiment and sentiment[0]:
            user_item["sentiment"] = sentiment[0].replace(u"\xa0", "")
        if vip_level and vip_level[0]:
            user_item["vip_level"] = vip_level[0].replace(u"\xa0", "")
        if authentication and authentication[0]:
            user_item["authentication"] = authentication[0].replace(u"\xa0", "")
        if labels and labels[0]:
            user_item["labels"] = labels[0].replace(u"\xa0", ",").replace(';', '').strip(',')
        education_info = selector.xpath('//div[contains(text(),"学习经历")]/following-sibling::div[1]'). \
            xpath('string(.)').extract()
        if education_info:
            user_item['education'] = education_info[0].replace(u"\xa0", "")
        work_info = selector.xpath('//div[contains(text(),"工作经历")]/following-sibling::div[1]'). \
            xpath('string(.)').extract()
        if work_info:
            user_item['work'] = work_info[0].replace(u"\xa0", "")
        request_meta = response.meta
        request_meta['item'] = user_item
        yield Request(self.base_url + '/u/{}'.format(user_item['_id']),
                      callback=self.parseuser_further_information,
                      meta=request_meta, dont_filter=True, priority=1, )

    def parseuser_further_information(self, response):
        text = response.text
        user_item = response.meta['item']
        tweets_num = re.findall('微博\[(\d+)\]', text)
        if tweets_num:
            user_item['tweets_num'] = int(tweets_num[0])
        follows_num = re.findall('关注\[(\d+)\]', text)
        if follows_num:
            user_item['follows_num'] = int(follows_num[0])
        fans_num = re.findall('粉丝\[(\d+)\]', text)
        if fans_num:
            user_item['fans_num'] = int(fans_num[0])
        yield user_item

    def parse_tweet(self, response):
        if response.url.endswith('page=1'):
            all_page = re.search(r'/>&nbsp;1/(\d+)页</div>', response.text)
            if all_page:
                all_page = all_page.group(1)
                all_page = int(all_page)
                for page_num in range(2, all_page + 1):
                    page_url = response.url.replace('page=1', 'page={}'.format(page_num))
                    yield Request(page_url, self.parse_tweet, dont_filter=True, meta=response.meta)
                # 如果是搜索接口，按照天的粒度结果已经是100页，那继续按照小时的粒度进行切分
                if 'search/mblog' in response.url and all_page == 100 and '-' not in response.url:
                    start_time_string = re.search(r'starttime=(\d+)&', unquote(response.url, "utf-8")).group(1)
                    keyword = re.search(r'keyword=(.*?)&', unquote(response.url, "utf-8")).group(1)
                    self.logger.info(f'split by hour,{start_time_string},{keyword}, {unquote(response.url, "utf-8")}')
                    date_start = datetime.datetime.strptime(start_time_string, "%Y%m%d")
                    time_spread = datetime.timedelta(days=1)
                    url_format_by_hour = "https://weibo.cn/search/mblog?hideSearchFrame=&keyword={" \
                                         "}&advancedfilter=1&starttime={}&endtime={}&sort=time&atten=1&page=1 "
                    one_day_back = date_start - time_spread
                    # from today's 7:00-8:00am to 23:00-24:00am
                    for hour in range(7, 24):
                        # calculation rule of starting time: start_date 8:00am + offset:16
                        begin_hour = one_day_back.strftime("%Y%m%d") + "-" + str(hour + 16)
                        # calculation rule of ending time: (end_date+1) 8:00am + offset:-7
                        end_hour = one_day_back.strftime("%Y%m%d") + "-" + str(hour - 7)
                        page_url = url_format_by_hour.format(keyword, begin_hour, end_hour)
                        yield Request(page_url, self.parse_tweet, dont_filter=True, meta=response.meta)
                    two_day_back = one_day_back - time_spread
                    # from today's 0:00-1:00am to 6:00-7:00am
                    for hour in range(0, 7):
                        # note the offset change bc we are two-days back now
                        begin_hour = two_day_back.strftime("%Y%m%d") + "-" + str(hour + 40)
                        end_hour = two_day_back.strftime("%Y%m%d") + "-" + str(hour + 17)
                        page_url = url_format_by_hour.format(keyword, begin_hour, end_hour)
                        yield Request(page_url, self.parse_tweet, dont_filter=True, meta=response.meta)

        tree_node = etree.HTML(response.body)
        tweet_nodes = tree_node.xpath('//div[@class="c" and @id]')
        for tweet_node in tweet_nodes:
            try:
                tweet_item = TweetItem()
                tweet_item['crawl_time'] = int(time.time())
                tweet_repost_url = tweet_node.xpath('.//a[contains(text(),"转发[")]/@href')[0]
                user_tweet_id = re.search(r'/repost/(.*?)\?uid=(\d+)', tweet_repost_url)
                tweet_item['weibo_url'] = 'https://weibo.com/{}/{}'.format(user_tweet_id.group(2),
                                                                           user_tweet_id.group(1))
                tweet_item['user_id'] = user_tweet_id.group(2)
                tweet_item['_id'] = user_tweet_id.group(1)
                create_time_info_node = tweet_node.xpath('.//span[@class="ct"]')[-1]
                create_time_info = create_time_info_node.xpath('string(.)')
                if "来自" in create_time_info:

                    tweet_item['created_at'] = datetime.datetime.strptime(
                        time_fix(create_time_info.split('来自')[0].strip()), '%Y-%m-%d %H:%M')
                    tweet_item['tool'] = create_time_info.split('来自')[1].strip()
                else:

                    tweet_item['created_at'] = datetime.datetime.strptime(time_fix(create_time_info.strip()),
                                                                          '%Y-%m-%d %H:%M')

                like_num = tweet_node.xpath('.//a[contains(text(),"赞[")]/text()')[-1]
                tweet_item['like_num'] = int(re.search('\d+', like_num).group())

                repost_num = tweet_node.xpath('.//a[contains(text(),"转发[")]/text()')[-1]
                tweet_item['repost_num'] = int(re.search('\d+', repost_num).group())

                comment_num = tweet_node.xpath(
                    './/a[contains(text(),"评论[") and not(contains(text(),"原文"))]/text()')[-1]
                tweet_item['comment_num'] = int(re.search('\d+', comment_num).group())

                images = tweet_node.xpath('.//img[@alt="图片"]/@src')
                if images:
                    tweet_item['image_url'] = images
                repost_node = tweet_node.xpath('.//a[contains(text(),"原文评论[")]/@href')
                if repost_node:
                    tweet_item['origin_weibo'] = repost_node[0]

                all_content_link = tweet_node.xpath('.//a[text()="全文" and contains(@href,"ckAll=1")]')
                if all_content_link:
                    all_content_url = self.base_url + all_content_link[0].xpath('./@href')[0]
                    yield Request(all_content_url, callback=self.parse_all_content, meta={'item': tweet_item},
                                  priority=1)
                else:
                    tweet_html = etree.tostring(tweet_node, encoding='unicode')
                    tweet_item['content'] = extract_weibo_content(tweet_html)
                    if tweet_item['content'] != '':
                        yield tweet_item

            except Exception as e:
                self.logger.error(e)

    def parse_all_content(self, response):
        tree_node = etree.HTML(response.body)
        tweet_item = response.meta['item']
        content_node = tree_node.xpath('//*[@id="M_"]/div[1]')[0]
        tweet_html = etree.tostring(content_node, encoding='unicode')
        tweet_item['content'] = extract_weibo_content(tweet_html)
        yield tweet_item
