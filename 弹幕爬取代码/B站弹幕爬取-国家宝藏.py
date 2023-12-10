'''
爬取B站视频弹幕内容
作者：李子航
'''
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
time_nature=[]
comments=[]

cid = input('请输入该B站视频的cid: ') #其中cid是弹幕对应的id
url = f'https://comment.bilibili.com/{cid}.xml' #这里是弹幕存储的url

print(url)

request = requests.get(url,verify=False)#获取页面
request.encoding='utf8'#因为是中文，我们需要进行转码，否则出来的都是unicode
soup = BeautifulSoup(request.text, 'lxml') 
results = soup.find_all('d')
for t in soup.find_all('d'):  # for循环遍历所有d标签，并把返回列表中的内容赋给t      
    time_nature.append(t.attrs['p'])            
    comments.append(t.text)              
    print(t.attrs['p']) 
    print(t.text)  

df = pd.DataFrame()
df['时间属性'] = time_nature
df['弹幕内容'] = comments

df.to_excel('C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\《国家宝藏》第四季第十期-弹幕.xls')
print('输出完成')