'''
requests.session 来保持状态。自动管理过程中产生的cookie，
下次请求时自动带上上一次的cookie
'''

import requests

# requests.get()
s = requests.session()
print(s.cookies)  # <RequestsCookieJar[]>
# 通过dict_from_cookiejar 将cookie 转成字典
print("登陆前的cookie:", requests.utils.dict_from_cookiejar(s.cookies))
# 登录接口
# r = s.post()
url = "https://www.bagevent.com/user/login"
cs ={
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=cs)
# print(r.text)

# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

# 退出登陆的接口
r = s.get("https://www.bagevent.com/user/login_out")
# print(r.text)
print("退出登陆后的cookie:", requests.utils.dict_from_cookiejar(s.cookies))
