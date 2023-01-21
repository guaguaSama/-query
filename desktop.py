import requests
import json
import re
import tkinter

headers = {
        #"Accept":"*/*",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip,deflate,br",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "57",
        "Content-Type": "application/x-www-form-urlencoded",
        #"Content-Type": "application/json",
        "Cookie": "Hm_lvt_2b20400ea9ae786e9eadaff65f314518=1674261180; Hm_lpvt_2b20400ea9ae786e9eadaff65f314518=1674261180",
        "Host": "chengyu.duwenz.com",
        "Origin": "https://chengyu.duwenz.com",
        "Referer": "https://chengyu.duwenz.com/",
        "sec-ch-ua":'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
        

data = {
        "en":"", 
        "erid":"", 
        "a": "getcysearch",
        "k1": "",
        "k2": "",
        "k3":"",
        "k4":"",
}
a=["k1","k2","k3","k4"]
for i in range(4):
        data[a[i]] = input("第%s个字:"%(i+1))

print(data)
        

#data=json.dumps(data)
#print(data)

#url = "http://www.jnqz.cn/search/"
url = "https://chengyu.duwenz.com/"
url = "https://chengyu.duwenz.com/manage/javaajax_cy.aspx"

#r = requests.post(url,headers=headers)
#r = requests.post(url)
#response = r.json()
#response = requests.post(url,data=data,headers=headers)
response = requests.post(url,headers=headers,data=data)
print(response.encoding)
response.encoding = 'utf-8'

print(response)
#print(response.text)
print(response.text)
#r = response.json()
#print(r)

print(type(response.text))


p = re.compile(r'target=_self>(.*?)</a>')
for i in p.findall(response.text):
        print(i)





