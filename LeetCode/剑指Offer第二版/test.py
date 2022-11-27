import requests
import json
import re

while True:
    user = input("请输入你的学小易账号：");
    password = input("请输入你的学小易密码：");
    print('正在登陆中...请稍等！')
    url0 = 'https://app.51xuexiaoyi.com/api/v1/login'
    data0 = {
        "username": user,
        "password": password
    }
    headers0 = {
        'platform': 'android',
        'app-version': '1.0.6',
        'content-type': "application/json; charset=utf-8",
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/3.11.0'
    }
    denglu = requests.post(url0, headers=headers0, json=data0).text.encode('utf-8').decode('unicode_escape')
    print(denglu)
    if '登录成功' in denglu:
        tokens = re.search(r'"api_token":"(.*)","userid"', denglu).group(1)
        # print(tokens)
        break
while True:
    a = input("请输入需要查的题目：");
    url = 'https://app.51xuexiaoyi.com/api/v1/searchQuestion'
    data = {
        'keyword': a
    }
    headers = {
        'token': tokens,
        'device': '',
        'platform': 'android',
        'User-Agent': 'okhttp/3.11.0',
        'app-version': '1.0.6',

        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept-Encoding': "gzip, deflate, br"
    }
    r = requests.post(url, headers=headers, data=data)
    # print(r1.json())

    html1_str = json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ':'))
    str = html1_str.encode('utf-8').decode('unicode_escape')
    forword = re.sub(r'"ey(.*)",', ' ', str)
    print(forword)