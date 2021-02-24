'''
pytest命名约束：
1、文件用test_开头
2、类用Test开头
3、函数或方法用test_开头
'''
import requests
url = "http://jy001:8081/futureloan/mvc/api/member/register"
# def test_register_001():
#     print("注册成功的脚本")
#     cs = {
#         "mobilephone": "15591464534",
#         "pwd": "123456",
#         "regname": "requests_test"
#     }
#     r = requests.get(url, params=cs)
#     # print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 1
#     assert rjson['code'] == '10001'  #'20110'
#     assert rjson["msg"] == "注册成功"
#     assert "成功" in r.text
#     print(r.text)
def test_register_002():
    print("手机号码格式不正确")
    for i in range(10):
        cs = {
         "mobilephone": "1559146453",
         "pwd": "123456",
         "regname": "requests_test"
        }

        r = requests.get(url, params=cs)
        rjson = r.json()
        assert rjson['status'] == 0
        assert rjson['code'] == '20109'
        assert rjson["msg"] == "手机号码格式不正确"
        assert "手机号码格式" in r.text
        print(r.text)

def test_register_003():
    print("密码不足5位")
    # for i in range()
    cs = {
        "mobilephone": "15591464532",
        "pwd": "12345",
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    # print(r.text)
    rjson = r.json()
    assert rjson['status'] == 0
    assert rjson['code'] == '20108'
    assert rjson["msg"] == "密码长度必须为6~18"
    assert "密码长度" in r.text
    print(r.text)
# def test_register_004():
#     print("手机号已注册")
#     cs = {
#         "mobilephone": "15591464532",
#         "pwd": "123456",
#         "regname": "requests_test"
#     }
#     r = requests.get(url, params=cs)
#     # print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20110'
#     assert rjson["msg"] == "手机号码已被注册"
#     assert "已被注册" in r.text
#     print(r.text)


# url = "http://jy001:8081/futureloan/mvc/api/member/login"
# def test_login_001():
#     print("登录成功")
#     cs = {"mobilephone": "15591464532", "pwd": "123456"}
#     r = requests.post(url, data=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 1
#     assert rjson['code'] == '10001'
#     assert rjson["msg"] == "登录成功"
#     assert "成功" in r.text

# def test_login_002():
#     print("登录失败")
#     cs = {"mobilephone": "1559146453", "pwd": "123456"}
#     r = requests.post(url, data=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20111'
#     assert rjson["msg"] == "用户名或密码错误"
#     assert "密码错误" in r.text
