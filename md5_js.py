import execjs
import os  
#执行本地的js  
  
def get_js():  
    # f = open("D:\python\js\md5.js",'r',encoding='UTF-8')  
    f = open("D:\python\js\md5.js", 'r', encoding='UTF-8')  
    line = f.readline()  
    htmlstr = ''  
    while line:  
        htmlstr = htmlstr + line  
        line = f.readline()  
    return htmlstr  
  
jsstr = get_js()  
ctx = execjs.compile(jsstr)  
print(ctx.call('calcMD5','888888'))  
os.system("PAUSE")
