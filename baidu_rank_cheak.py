import requests, time, math
from lxml import html
from urllib.parse import urlparse
from datetime import datetime
from pymongo import MongoClient
from multiprocessing.dummy import Pool
client = MongoClient()
baidu = client['baidu']
paurl = baidu['paurl']

"""
百度关键词排名监控
1、遍历关键词排列，记录真实的URL和排名的位置，更新到数据库中
"""

base_url = 'http://www.baidu.com/s?ie=UTF-8&wd={keyword}&rn={pagenum}&pn={pagenext}'
RESULTS = {}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

def parse_url(parseurl, retries=1):
    try:
        res = requests.head(parseurl, timeout=3).headers
        print(parseurl)
    except Exception as e:
        # print("解密URL出异常",e)
        # print("重试中，第{}次".format(retries))
        time.sleep(10)
        if retries <= 10:
            return parse_url(parseurl, retries+1)
        else:
            print("返回空值", retries)
            return None
    else:
        return res.get("Location")


def getList(my_domain,keyword, num=50, nextpage=0, isflag=False):
    try:
        res = requests.get(base_url.format(keyword=keyword, pagenum=num, pagenext=nextpage))
        uu = base_url.format(keyword=keyword, pagenum=num, pagenext=nextpage)
        source = res.content
    except Exception:
        time.sleep(8)
        getList(my_domain, keyword, nextpage=nextpage, isflag=isflag)
    else:
        flag = isflag
        if res.status_code == 200:
            selector = html.fromstring(source)
            if verify(selector.xpath("//title/text()")):
                urls = selector.xpath("//*[@id]/h3/a/@href")
                ranks = selector.xpath("//*[@id]/h3/../@id")
                for url, rank in zip(urls, ranks):
                    real_link = parse_url(url)
                    domain_link = urlparse(real_link).netloc
                    if str(domain_link).endswith(my_domain):
                        data = {
                            "keyword": keyword,
                            'real_link': real_link,
                            'rank': rank,
                            'where': "http://www.baidu.com/s?wd={}&rn={}&pn={}#{}".format(keyword, num, (
                            math.ceil((int(rank) / num)) - 1) * num, rank),
                            'date': datetime.now().date().strftime("%Y-%m-%d")
                        }
                        print(data)
                        if paurl.find({"keyword": data['keyword'], 'real_link': data['real_link'],
                                       'date': data['date']}).count() < 1:
                            paurl.insert_one(data)
                        flag = True
                if not flag and nextpage == 50:
                    data = {
                        "keyword": keyword,
                        'real_link': None,
                        'rank': 0,
                        'where': None,
                        'date': datetime.now().date().strftime("%Y-%m-%d")
                    }
                    print(data, nextpage)
                    if paurl.find({"keyword": data['keyword'], 'real_link': data['real_link'],
                                   'date': data['date']}).count() < 1:
                        paurl.insert_one(data)

            else:
                time.sleep(5)
                getList(my_domain, keyword)

            if nextpage != 50:
                getList(my_domain, keyword, num=50, nextpage=50, isflag=flag)
        else:
            time.sleep(10)
            getList(my_domain, keyword, nextpage=nextpage, isflag=flag)

def verify(webtitle):
    return str(webtitle[0]).endswith("百度搜索") if webtitle else False


def getalldata(keywor):
    getList(search_link, keywor)

if __name__ == '__main__':
    pool = Pool(30)
    search_link = "paurl.com"
    pool.map(getalldata,
             ["伯乐运营",'运营自学网','运营','运营培训','互联网运营', '互联网运营管理',"网站运营","网站运营管理",'运营管理','网站运营管理','互联网运营培训',
              '运营书籍推荐',"互联网运营学习",'互联网运营培训网','网站运营培训', "网站管理及运营",'运营管理培训'])

    # getalldata("互联网运营")