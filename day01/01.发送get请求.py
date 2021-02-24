'''
接口测试：
    使用requests中的get、post方法调用接口，检查返回值是否正确。
'''

import requests

#获取用户列表

#############################get请求，不带参数################################
url = "http://jy001:8081/futureloan/mvc/api/member/list"
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
# 发送get请求
r = requests.get(url)
# 打印响应
print(r.text)
# 检查结果是否与与预期相同
assert r.status_code == 200   # 断言
assert r.reason == "OK"
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'
assert rjson["msg"] == "获取用户列表成功"
# 响应头
print(r.headers)

#############################get请求，带参数################################
# 注册接口，参数拼接在URL的后面，?后面是参数，多个参数使用&连接
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15591464532&pwd=123456"
# 发送get请求
r = requests.get(url)
# 打印响应
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20110'
assert rjson["msg"] == "手机号码已被注册"
# 响应头
print(r.headers)

#############################get请求，带参数################################
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=1559146453&pwd=12345"
# 发送get请求
r = requests.get(url)
# 打印响应
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20108'
assert rjson["msg"] == "密码长度必须为6~18"

#注册接口 ，使用param参数
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs ={
    "mobilephone": "15591464532",
    "pwd": "123456",
    "regname": "requests_test"

}
r = requests.get(url, params=cs)
print(r.text)
rjson = r.json()
assert rjson['status'] == 0
assert rjson['code'] == '20110'
assert rjson["msg"] == "手机号码已被注册"

# 查询手机号码归属地的接口，参数:tel
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15591464532"
r = requests.get(url)
print(r.text)
# print(r.json()) # 报错，因为返回的结果不是json格式
assert '陕西联通' in r.text
