import requests

# 表单格式的数据：content-type:www-x-form-urlencoded，使用data传参
# 登录接口

url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "15591464532", "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'
assert rjson["msg"] == "登录成功"



# json格式的数据：content-type:application/json，使用json传参
# 具体使用data 还是 json 传参，要看接口是怎么定义的。
# httpbin.org 是一个测试网站，不管发送什么类型的数据，
# 这个接口将发送的请求，封装成json 格式的返回
url = "http://www.httpbin.org/post"
cs = {"mobilephone": 15591464532, "pwd": "123456"}
r = requests.post(url, data=cs)
print("data传参===", r.text)
r = requests.post(url, json=cs)
print("json传参===", r.text)

# 租车系统，添加车辆
url = "http://127.0.0.1:8080/carRental/car/addCar.action"
cs = {"carnumber": "20000",
      "cartype": "20000",
      "color": "20000",
      "carimg": "images/defaultcarimage.jpg",
      "description": "20000",
      "price": 20000,
      "rentprice": 10000,
      "deposit": 1000,
      "isrenting": 0}

# 使用脚本添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
# 分别抓脚本的包与界面的包，对比差异。界面设置了charset=UTF-8，但是脚本未设置导致。
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

# Fiddler 抓脚本的包，设置代理
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888", #https协议，使用这个代理
}
r = requests.post(url, data=cs, proxies=proxy)
print(r.text)
