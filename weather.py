#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 天气爬虫
import requests
import math
from bs4 import BeautifulSoup

def get_weather(url):
    str = '/'
    if url.find(str)>= 0:
        url = "http://qq.ip138.com/weather/" + url +".htm"
    else:
        url = "http://qq.ip138.com/weather/" + url +"/"
   
    # 定义header
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    # 发起请求
    req = requests.get(url,headers=header)
    # 字符编码
    req.encoding = 'GB2312'
    # print(req.text)
    # 创建BeautifulSoup对象
    bs = BeautifulSoup(req.text,"html.parser")
    body = bs.body
    # print(body)
    data = body.find('table',{'class':'t12'})
    # print(data)
    tr = data.find_all('tr')
    wtdata = []
    b = ' '
    n = 16
    for tdall in tr:
        if len(tdall) > 5:
            td = tdall.find_all('td')
            data = []
            for tdcon in td:
                if tdcon.string == None:
                    tdtext = "|"+ b*math.ceil((n-len(tdcon.find('img').attrs["alt"]))/2) +tdcon.find('img').attrs["alt"]+b*math.floor((n-len(tdcon.find('img').attrs["alt"]))/2)
                    print(tdtext , end = ' ')
                else:
                    tdtext = "|"+ b*math.ceil((n-len(tdcon.string))/2) +tdcon.string+b*math.floor((n-len(tdcon.string))/2)
                    print(tdtext , end=' ')
            # 输出换行
            print("|")
            print(end="\n")


if __name__ == '__main__':
    # 地址取url
    # 内蒙古赤峰    neimenggu/ChiFeng
    # 上海长宁      shanghai/changning
    # 上海宝山      shanghai/Baoshan
    # 上海浦东      shanghai/pudongxinqu
    url = 'shanghai/pudongxinqu'
    get_weather(url)
        