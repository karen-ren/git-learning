# -*- coding=utf-8 -*-
import json

import requests

header = {
    'User-Agent': 'googlespider',
    'Content-Encoding': 'gzip',
    'X-Forwarded-For': '202.101.43.22',
}


class Business(object):
    def __init__(self):
        pass

    def my_problem_and_solution(self):
        """我的问题所在及解决方式，是request返回数据的编码解码问题，主要在这个生僻汉字'碶'上"""
        url = "https://dealer.autohome.com.cn/Ajax/GetDealerInfo?DealerId=2052112"

        r = requests.get(url=url, headers=header)
        try:
            response = r.content.decode('utf-8')
        except UnicodeDecodeError:
            response = r.content.decode('GB18030')

        # 将json字符串转为python的字典
        body = json.loads(response)
        print(body, '\n', type(body))


if __name__ == "__main__":
    b = Business()
    b.my_problem_and_solution()
