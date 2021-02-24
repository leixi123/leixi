import requests

# 接口路径
url = "http://www.httpbin.org/post"
# # 本地存在的文件
# file = "e:/test.png"
# # rb二进制制度的方式打开
# with open(file, mode='rb')as f:
#     # {'name':file - tuple}
#     # {'filename', fileobj,'content_type'}
#     cs = {'filename': (file, f, "image/png")}
#     r = requests.post(url, files=cs)
#     print(r.text)

# 租车系统上传图片
url = "http://127.0.0.1:8080/carRental/file/uploadFile.action"
file = "e:/test.png"
with open(file, mode='rb')as f:
    # {'name':file - tuple}
    # {'filename', fileobj,'content_type'}
    cs = {'mf': (file, f, "image/png")}
    r = requests.post(url, files=cs)
    #{"code": 0, "msg": "", "count": null, "data": {"src": "2021-01-28/202101281428381599404.png_temp"}}
    uploadPath = r.json()['data']['src']
#添加车，使用刚上传的图片
url = "http://127.0.0.1:8080/carRental/car/addCar.action"
cs = {"carnumber": "40000",
      "cartype": "40000",
      "color": "40000",
      "carimg": uploadPath,
      "description": "40000",
      "price": 20000,
      "rentprice": 10000,
      "deposit": 1000,
      "isrenting": 0}
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888", #https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=head, proxies=proxy)
print(r.text)