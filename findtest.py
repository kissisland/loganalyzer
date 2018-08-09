import requests, time
import csv, re
from lxml import html
from urllib.parse import urljoin
from multiprocessing.dummy import Pool

from pymongo import MongoClient

client = MongoClient()
kuaijiwang = client['kuaijiwang']
article_url = kuaijiwang['article_url']
article_status = kuaijiwang['article_status6']

bbs_url = kuaijiwang['bbs_url']
bbs_status = kuaijiwang['bbs_status3']


start_url = 'http://zmt.kuaiji.com/portal/list/seoCheckList?page={}'
bbs_starturl = 'http://bbs.kuaiji.com/forum.php?mod=guide&view=check&page={}'

def save_file(dic):
    file = open("false_file10.csv", 'a', encoding='utf-8', newline='')
    writer = csv.DictWriter(file, fieldnames=['title', 'url', 'tag'])
    writer.writerow(dic)

def check(con):
    this_data = []
    for item in ["网盘","迅雷","种子","旋风","BT","115","下载",".rar"," .pdf"," .exe"," .zip ",".doc",".docx","ppt","xls",'xlsx',"pan.baidu.com"]:
        if item in con:
            this_data.append(item)
    if this_data:
        return False, '，'.join(this_data)
    else:
        return True,"没"

def check2(con):
    match = re.search(r'\[url=(http://.*?(?!kuaiji)*?(com|net|cn|org))\]', con, re.S)
    if match:
        return False, match.group()
    else:
        return True, "没有"

def get_list_url(url):
    try:
        # res = requests.get(url)
        # if res.status_code == 200:
        #     selector = html.fromstring(res.content)
        #     url_list = selector.xpath("//ul[@class='list']/li/a/@href")
        #     # return [urljoin(url, link) for link in url_list]
        #     for u in [urljoin(url, link) for link in url_list]:
        #         article_url.insert_one({
        #             "url":u,
        #             'status':0
        #         })
        #         print(u)
        res = requests.get(url)
        if res.status_code == 200:
            selector = html.fromstring(res.content)
            url_list = selector.xpath("//ul[@class='list']/li/a/@href")
            # for i in url_list:
            #     print(urljoin(url, i))
            for u in [urljoin(url, link) for link in url_list]:
                bbs_url.insert_one({
                    "url":u,
                    'status':0
                })
                print(u)
        else:
            print("访问超时了.....")
            return get_list_url(url)
    except Exception as e:
        print(e)
        return get_list_url(url)

def get_detail(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            res.encoding = "utf-8"
            selector = html.fromstring(res.text)
            # title = selector.xpath("//h2/text()")
            title = selector.xpath("//ul/li[2]/span[@class='title']/text()")
            if title:
                title = title[0]
            content = selector.xpath("//ul")
            if content:
                # content = html.tostring(content[0], encoding='utf-8').decode()
                content = selector.xpath("string(.)")
            flag = check(content)
            if not flag[0]:
                data = {
                    'title':title,
                    'url':url,
                    'tag':flag[1]
                }
                print(title, url)
                save_file(data)
            else:
                print(url, "未命中", title)

            bbs_status.insert_one({'url':url, 'status':1})
        else:
            print("访问超时了.....")
            return get_detail(url)

    except Exception as e:
        print(e, url)
        return get_detail(url)

if __name__ == '__main__':
    pool = Pool(100)
    # for i in range(1, 464):
    #     pool.map(get_detail, get_list_url(start_url.format(i)))

    # pool.map(get_list_url, [bbs_starturl.format(i) for i in range(1, 339)])
    pool.map(get_detail, [i['url'] for i in bbs_url.find()])
    # get_detail("http://bbs.kuaiji.com/forum.php?mod=guide&view=check_detail&id=11459")
    # pool.map(get_detail, list(set([i['url'] for i in article_url.find()]).difference(set([i['url'] for i in article_status.find()]))))
    # for i in list(set([i['url'] for i in article_url.find()]).difference(set([i['url'] for i in article_status.find()]))):
    #     print(i)
    # data_urls = []
    # with open("false_file4.csv", 'r')as f:
    #     for i in csv.DictReader(f):
    #         data_urls.append(i['url'])
    # pool.map(get_detail, data_urls)

    # get_detail("http://zmt.kuaiji.com/portal/list/seoCheckDetail/id/3327042")