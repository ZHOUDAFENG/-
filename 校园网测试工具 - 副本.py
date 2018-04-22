#coding=utf-8   
import requests
from bs4 import BeautifulSoup
import re

def find_checkcode ():
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
    #用get方法打开url并发送headers
    html = requests.get(url,headers = header) 
    soup = BeautifulSoup(html.text,'html.parser')
    _checkcode = soup.find_all('script')
    return (re.findall("\d\d\d\d", _checkcode[5].text)[5])



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
    html2 = requests.post(url,headers=header,data=post_Data)
    print(html2)
    soup2 = BeautifulSoup(html2.text,'html.parser')
    print(soup2)

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
    soup = BeautifulSoup(html.text,'html.parser')
    _checkcode = soup.find_all('script')
    return (re.findall("\d\d\d\d", _checkcode[5].text)[5])
    

if __name__ == '__main__':

    Cookies='mySkin=style%2Fblue%2F; JSESSIONID=5125768E12C08FE8D63DA1E43978686B'

    b=find_checkcode ()
    post_login (b,'LTB20170302117')
    b=logout ()
    post_login (b,'LTB20170302215')
    b=logout ()


<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<title>用户自助服务系统</title><!-- 001pubtags=用户自助服务系统 -->
<link rel="stylesheet" skin="true" skinresource="css/main.css" type="text/css"/>
<link rel="stylesheet" skin="true" skinresource="css/index.css" type="text/css"/>
<script src="js/jquery-1.6.js" type="text/javascript"></script>
<script src="js/jqueryCookie.js" type="text/javascript"></script>
<script src="js/pub.js" type="text/javascript"></script>
<script src="js/skin.js" type="text/javascript"></script>
</head>
<script charset="utf-8" type="text/javascript">
			$(document).ready(function() {
				//var btip='false';
				var btip=$("#btip").val();
				if (btip=="true"){
					if(confirm('您还没有设置密码保护问题，现在设置吗？')){//0001_main.jsp=您还没有设置密码保护问题，现在设置吗？
						window.location.href="nav_Question";
					}
				}
				$("#btip").val("false");
			})
		</script>
<body style="display: none;">
<div class="body2">
<input id="leftflag" type="hidden" value="0"/>
<div class="outbox">
<!-- 页头 -->
<div class="header"><img skin="true" skinresource="images/logo/logo.gif"/>
<span class="skin">
<a href="##">
<img border="0" id="skinBtn" skin="true" skinresource="images/skin.gif" title="换肤"/><!-- 002pubtags=换肤 -->
</a>
</span>
</div>
<div class="skin_boxout" id="skinSelector">
<div class="skin_boxin">
<div class="skin_context" id="skin_context">
<img src="images/loading.gif" title="加载中"/><!-- 003pubtags=加载中 -->
</div>
</div>
<img id="currentSkin_icon" src="images/done-square.gif"/>
</div>
<!-- 内容 -->
<div class="content_bg">
<div class="content_top">
<div class="content_bom">
<!-- 左栏 -->
<div class="leftbox">
<!-- 帐户信息 -->
<div class="info_bg"><!-- 背景 -->
<div class="info_top"><!-- 背景上图 -->
<div class="info_bom"><!-- 背景下图 -->
<div class="info_title">帐户信息</div><!-- 0001_left.jsp=帐户信息 -->
<div class="info_text">
<!-- 2011/11/14帐号更改为账号 -->
			账号：<span class="account">LTB20170302215(彭涛)</span><br/><!-- 0002_left.jsp=账号： -->
			套餐：<span class="service"></span><br/><!-- 0003_left.jsp=套餐： -->
			
			
			余额：<span class="redtext"><span class="redtextl"></span></span> (<span class="urltext"><a href="nav_Rcard">快速充值</a></span>)<br/><!-- 0004_left.jsp=余额： --><!-- 0005_left.jsp=快速充值 -->
			状态：<span class="greentext"><!-- 0006_left.jsp=状态： -->
<span class="greentextl"></span><input id="userStatus" type="hidden" value="1"/>
</span>  
				 <span class="greentext21"><a href="nav_offLine">在线</a></span><span class="greentext20">离线</span><br/><!-- 0007_left.jsp=在线 --><!-- 0009_left.jsp=离线 -->
			
				防伪信息：<span class="checkcode1"><a href="nav_changeUserInfo">未设置              </a></span><!-- 0010_left.jsp=防伪信息： --><!-- 0011_left.jsp=未设置 -->
<span class="checkcode2"></span>
</div>
<input class="button" id="logout" name="Submit" type="button" value="退 出"/><!-- 0013_left.jsp=退 出 -->
</div>
</div>
</div>
<!-- 类目 -->
<div class="leftmenu_bg"><!-- 背景 -->
<div class="leftmenu_bom"><!-- 背景下图 -->
<div class="leftmenu_top"><!-- 背景上图 -->
<ul class="menu">
<li serial="0"><a href="nav_main">首页导航</a></li><!-- 005pubtags=首页导航 -->
<li serial="2"><a href="nav_mainQuery">查询服务</a></li><!-- 010pubtags=查询服务 -->
<li serial="3"><a href="nav_business">业务办理</a></li><!-- 006pubtags=业务办理 -->
</ul>
</div>
</div>
</div>　　<!-- 导入我的帐户页面 -->
</div>
<!-- 右栏 -->
<div class="rightbox">
<!-- 首页模块 -->
<!-- 透明外边 -->
<div class="t_boxout">
<div class="banner_bg">
<div class="banner_l">
<div class="banner_r">您现在的位置：<a href="nav_main">首页导航</a></div><!-- 004pubtags=您现在的位置： --><!-- 005pubtags=首页导航 -->
</div>
<div class="t_boxin"><!-- 内边框 -->
<input id="btip" name="btip" type="hidden" value="false"/>
<div class="iconmenu">
<div class="boxspacing">
<div class="info"><span class="fl"><a href="nav_mainQuery"><img border="0" skin="true" skinresource="images/inquiry.gif" title="查询服务"/></a></span><!-- 010pubtags=查询服务 -->
<span class="fr"> <b><a href="nav_mainQuery">查询服务</a></b>为您提供上网清单等多项查询服务。</span><!-- 010pubtags=查询服务 --><!-- 0003_main.jsp=为您提供上网清单等多项查询服务。 -->
</div>
<ul>
<li>·<a href="nav_getUserInfo">个人资料</a></li><!-- 0004_main.jsp=个人资料 -->
<li>·<a href="nav_monthPay">扣费账单</a></li><!-- 0005_main.jsp=扣费账单 -->
<li>·<a href="nav_operatorLog">业务办理记录</a></li><!-- 0006_main.jsp=业务办理记录 -->
<li>·<a href="nav_loginLog">上网详单</a></li><!-- 0007_main.jsp=上网详单 -->
<li>·<a href="nav_Payment">交费情况</a></li><!-- 0008_main.jsp=交费情况 -->
</ul>
</div>
</div>
<div class="iconmenu">
<div class="boxspacing">
<div class="info"><span class="fl"><a href="nav_business"><img border="0" skin="true" skinresource="images/handle.gif" title="业务办理"/></a></span> <!-- 006pubtags=业务办理 -->
<!-- 2011/11/14 修改为：锁定--报停、解锁--复通 -->
<span class="fr"> <b><a href="nav_business">业务办理</a></b>为您提供预约报停、预约套餐等多项服务。</span><!-- 006pubtags=业务办理 --><!-- 0009_main.jsp=为您提供预约报停、预约套餐等多项服务。 -->
</div>
<ul>
<li>·<a href="nav_changeUserInfo">修改资料</a></li><!-- 0010_main.jsp=修改资料 -->
<li>·<a href="nav_changePsw">修改密码</a></li><!-- 014pubtags=修改密码 -->
<li>·<a href="nav_selfStopReopen">预约报停/复通</a></li><!-- 0011_main.jsp=预约报停/复通 -->
<li>·<a href="#" name="openOrStopNow">立即报停/复通</a></li><!-- 0012_main.jsp=立即报停/复通 -->
<li>·<a href="nav_Question">设置密码保护</a></li><!-- 0014_main.jsp=设置密码保护 -->
<li>·<a href="nav_GetUserBindingPackageAction">绑定运营商账号</a></li><!-- 017pubtags=绑定运营商账号 -->
</ul>
</div>
</div>
</div>
</div>
</div>
<!-- 温馨提示 -->
<div class="tips_bg"><!-- 背景 -->
<div class="tips_top"><!-- 背景上图 -->
<div class="tips_bom"><!-- 背景下图 -->
<div class="tips_title">温馨提示：</div><!-- 009pubtags=温馨提示： -->
<div class="tips_text">宽带自助服务系统为您提供如下功能：<br><!-- 0016_main.jsp=宽带自助服务系统为您提供如下功能： -->
									1. 查看最新的通知、公告消息；<br><!-- 0017_main.jsp=1. 查看最新的通知、公告消息； -->
									2. 自助查询个人资料、充值缴费、上网详单、扣费账单、业务办理等记录；<br><!-- 0018_main.jsp=2. 自助查询个人资料、充值缴费、上网详单、扣费账单、业务办理等记录； -->
									3. 自助办理修改密码、个人资料变更、报停、复通、变更套餐及相关预约业务的申请等；<br><!-- 0019_main.jsp=3. 自助办理修改密码、个人资料变更、报停、复通、变更套餐及相关预约业务的申请等； -->
									4. 查看宽带产品的资费信息，方便您选用合适的套餐。<br/><!-- 0020_main.jsp=4. 查看宽带产品的资费信息，方便您选用合适的套餐。 -->
</br></br></br></br></div>
</div>
</div>
</div>
<div class="tips_bom2"></div>
</div>
</div>
<!-- 中下 -->
<div class="cenbom"></div>
</div>
</div>
</div>
<!-- 页脚 -->
<div class="footer">Power by CITYHOTSPOT</div>
</div>
</body>
</html>






    
