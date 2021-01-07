# encoding:utf-8
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Cookie': 'kv=eyJBY2NvdW50Q29kZSI6IjM2NDE3X2NqbCIsIlBhc3N3b3JkIjoiODg4ODg4In0=; Path=/; Domain=.www.safetyhua.com; Expires=Fri, 22 Jan 2021 05:02:35 GMT;ASP.NET_SessionId=egeoxibi2mva5nrwz0cle3xy;',
}

list_url = "http://www.safetyhua.com/DangerTemplate/GetPageData?TemplateType=Sys&order=asc&offset=0&limit=20&page=0&conditions=%5B%7B%22Name%22%3A%22profession%22%2C%22Value%22%3A%22IAPT00001%22%7D%2C%7B%22Name%22%3A%22ApplyArea%22%2C%22Value%22%3A%22%E5%B9%BF%E4%B8%9C%E7%9C%81%2F%E6%B7%B1%E5%9C%B3%E5%B8%82%22%7D%2C%7B%22Name%22%3A%22Title%22%2C%22Value%22%3A%22%22%7D%5D&_=1609996653532"
session = requests.Session()
response1 = session.get(list_url, headers=headers)
obj_list = json.loads(response1.text);
print(response1.status_code)
print(response1.text)
for data in obj_list['data']:
    tcode = data['TCode']
    detail_url = 'http://www.safetyhua.com/DangerTemplate/DetailView?tCode=%s' % tcode

    response = session.get(detail_url, headers=headers)
    detail_f = open('公共检查表库/%s.html' % tcode, mode='w',encoding='utf-8')
    print(response.status_code)
    if response.status_code == 200:
        detail_f.write(response.content.decode('utf-8'))
        print("----", tcode, "------")
