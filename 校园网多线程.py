#coding=utf-8
import xlrd
import xlwt
import requests
from bs4 import BeautifulSoup
import re
import time ,os
import random
def find_checkcode ():
    print("首页获取随机数字")
    url = 'http://lt.ccsu.cn/LoginAction.action'
    header ={
        
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie':Cookies,
        'Host':'lt.ccsu.cn',
        'Pragma': 'no-cache',
        'Referer':'http://lt.ccsu.cn/nav_main',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
        }
    html = requests.get(url,headers = header)
    
    soup = BeautifulSoup(html.text,'html.parser')
    _checkcode = soup.find_all('script')
    if(len(re.findall("\d\d\d\d", _checkcode[5].text))==6):
        return (re.findall("\d\d\d\d", _checkcode[5].text)[5])
    else:
        refresh()

        
def post_login (checkcode,account):
    
    url = 'http://lt.ccsu.cn/LoginAction.action'
    header={
        'Accept':                    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':           'gzip, deflate',
        'Accept-Language':           'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':                'keep-alive',
        'Content-Length':            '112',
        'Content-Type':              'application/x-www-form-urlencoded', 
        'Cookie':                    Cookies,     
        'Host':                      'lt.ccsu.cn',
        'Referer':                   'http://lt.ccsu.cn/LogoutAction.action',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'      

            }
    post_Data ={
        'account':account,
        'password':'e10adc3949ba59abbe56e057f20f883e',
        'code':'',
        'checkcode':checkcode,
        'Submit':'%E7%99%BB+%E5%BD%95'
        
        }
    html = requests.post(url,headers=header,data=post_Data)
    soup = BeautifulSoup(html.text,'html.parser')
    
    if(soup.find_all('span')!= []):
        txt_=str(soup.find_all('span')[1].text)
        print(soup.find_all('span')[1].text+"登陆成功")
        
        how_(txt_)
        return 0
    else:
        print(account+"不符合")
        return -1

def logout ():
    url='http://lt.ccsu.cn/LogoutAction.action'
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':'keep-alive',
        'Cookie':Cookies,
        'Host':'lt.ccsu.cn',
        'Referer':'http://lt.ccsu.cn/LoginAction.action',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
        }
    html = requests.get(url,headers = header)    
    print("退出")
    refresh()
        
        

def refresh():
    
    url="http://lt.ccsu.cn/nav_login"
        
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':'keep-alive',
        'Cookie':Cookies,
        'Host':'lt.ccsu.cn',
        'Referer':'http://lt.ccsu.cn/LoginAction.action',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
        }
    html = requests.get(url,headers=header)
    soup = BeautifulSoup(html.text,'html.parser')
    _checkcode = soup.find_all('script')
    if(len(re.findall("\d\d\d\d", _checkcode[5].text))==6):
        return (re.findall("\d\d\d\d", _checkcode[5].text)[5])
    else:
        refresh()
def how_(account):
    
    url="http://lt.ccsu.cn/nav_GetUserBindingPackageAction"
        
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':'keep-alive',
        'Cookie':Cookies,
        'Host':'lt.ccsu.cn',
        'Referer':'http://lt.ccsu.cn/nav_busines',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
        }
    html = requests.get(url,headers=header)
    soup = BeautifulSoup(html.text,'html.parser')
    if(soup.find_all('input')[3]['value']!=''):
        print(account+"绑定了账号")
        os.system("echo "+account+">> test1.txt")
def login_one ():
    check_code=refresh()
    url = 'http://lt.ccsu.cn/LoginAction.action'
    header={
        'Accept':                    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':           'gzip, deflate',
        'Accept-Language':           'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection':                'keep-alive',
        'Content-Length':            '112',
        'Content-Type':              'application/x-www-form-urlencoded', 
        'Cookie':                    Cookies,     
        'Host':                      'lt.ccsu.cn',
        'Referer':                   'http://lt.ccsu.cn/LogoutAction.action',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'      

            }
    post_Data ={
        'account':'LTB20170301111',
        'password':'e10adc3949ba59abbe56e057f20f883e',
        'code':'',
        'checkcode':check_code,
        'Submit':'%E7%99%BB+%E5%BD%95'
        
        }
    html = requests.post(url,headers=header,data=post_Data)
    soup = BeautifulSoup(html.text,'html.parser')
    
    logout ()

    
if __name__ == '__main__':
    
    Cookies='mySkin=style%2Fblue%2F; JSESSIONID=C2E36D5A117A1598A81962F44604713B'
    new_checkcode=find_checkcode ()
    working_xl = xlrd.open_workbook(r"D:\python\js\xl.xlsx")
    sheet_one = working_xl.sheet_by_index(0)
    col_=sheet_one.col_values(1)
    for name in col_:
        if(name!='学号'):
            if(post_login (new_checkcode,'LT'+name)==0):
                new_checkcode=logout ()
                new_checkcode=refresh()
            else:
                login_one ()
                new_checkcode=refresh()
            







    
