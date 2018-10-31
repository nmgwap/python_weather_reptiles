#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 获取城市信息
import requests
import math
from bs4 import BeautifulSoup

class getcity:

    # 初始化方法
    def __init__(self):
        self.url = "http://qq.ip138.com/weather/"
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
        # 省份信息
        self.provinces = ''
        # 选择的省份编码
        self.provincesNo = ''
        # 地区信息
        self.region = ''
        # 选择的地区编码
        self.regionNo = ''

    # 获取省份
    def getprovinces(self):
        print("获取省份中，请稍等...")
        # 发起请求
        req = requests.get(self.url,headers=self.header)
        # 字符编码
        req.encoding = 'GB2312'
        # 创建BeautifulSoup对象
        bs = BeautifulSoup(req.text,"html.parser")
        body = bs.body
        data = body.find('table',{'class':'t12'})
        td = data.find_all('td')
        listdata = []
        for list in td:
            dict = {}
            dict['url'] = list.find('a').attrs['href']
            dict['provinces'] = list.find('a').text
            listdata.append(dict)
        self.provinces = listdata

    # 输出
    def outputprovinces(self):
        print("省份获取成功")
        for prv in range(len(self.provinces)):
            if prv == 34:
                return
            print("编号:",prv,"=>",self.provinces[prv]['provinces'])

    # 获取用户输入
    def getinput(self):
        userinput = input("请输入对应的编号：");
        print("您输入的是",userinput)
        self.provincesNo = userinput

    # 获取地区
    def getregion(self):
        if int(self.provincesNo) > len(self.provinces) or int(self.provincesNo) < 0:
            return print("输入有误,请重新运行！")
        print("正在帮您获取地区信息，请稍等...")
        url = "http://qq.ip138.com" + self.provinces[int(self.provincesNo)]['url']
        req = requests.get(url,headers=self.header)
        # 字符编码
        req.encoding = 'GB2312'
        # 创建BeautifulSoup对象
        bs = BeautifulSoup(req.text,"html.parser")
        body = bs.body
        data = body.find('table',{'class':'t12'})
        td = data.find_all('td')
        listdata = []
        for list in td:
            dict = {}
            if list.find('a') != None:
                if list.find('a').string != None:
                    dict['url'] = list.find('a').attrs['href']
                    dict['region'] = list.find('a').text  
            listdata.append(dict)
        self.region = listdata 

    # 输出地区
    def outputregion(self):
        print("省份地区获取成功")
        for prv in range(len(self.region)):
            if self.region[prv] != {}:
                print("编号:",prv,"=>",self.region[prv]['region']) 

    # 获取用户输入
    def getinputregion(self):
        userinput = input("请输入对应的编号：");
        print("您输入的是",userinput)
        self.regionNo = userinput

    # 获取选择地区的天气
    def getregionweater(self):
        if self.region[int(self.regionNo)] == {}:
            return print("对不起，编号不存在！")
        if int(self.regionNo) > len(self.region) or int(self.regionNo) < 0:
            return print("输入有误,请重新运行！")
        print("请稍等，正在帮您获取",self.region[int(self.regionNo)]['region'],"的天气")
        url = "http://qq.ip138.com" + self.region[int(self.regionNo)]['url']
        # 发起请求
        req = requests.get(url,headers=self.header)
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
        print("天气获取成功！")
# 自调
if __name__ == "__main__":
    print("启动程序")
    # 实例化
    city = getcity()
    # 调用
    city.getprovinces()
    city.outputprovinces()
    city.getinput()
    city.getregion()
    city.outputregion()
    city.getinputregion()
    city.getregionweater()
