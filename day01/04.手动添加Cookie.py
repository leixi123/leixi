'''
Cookie 识别用户
'''

import requests
#没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上cookie信息
head = {
"Cookie": '_ga=GA1.2.2127613074.1611729444; __auc=390b6ead177428fa3ec0d236000; MEIQIA_TRACK_ID=1ndqkOvLTODrzzicRXB39UzugVM; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611729444,1611818344; __asc=458f7e3517747dc235d89a581fd; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1611729446,1611818349; MEIQIA_VISIT_ID=1ngitakSaxiHlZmehWA1ehiAeez; _gid=GA1.2.776782581.1611818415; BAGSESSIONID=250085ba-a2c1-427e-b5b5-b2e7c5bc21ee; JSESSIONID=6138F63EC01F0AB2498F9952846DC8DA; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818900; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1611818901'
}
r = requests.get(url, headers=head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：
1、cookie 会失效，失效后需要重新获取
2、登陆后的每个接口，需要带着cookie
'''
