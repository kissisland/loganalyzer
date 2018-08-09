import requests
import time, urllib.parse
from lxml import html
from multiprocessing.dummy import Pool
base_url = 'http://www.kuaiji.com/hot'
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}
i = 1
bad_url = []
def getHtml(url):
    global i
    try:
        start = time.time()
        res = requests.get(url, timeout=60)

        if res.status_code != 200:
            bad_url.append(url)
            # return getHtml(url)

    except Exception as e:
        print(url, "异常", e)
        return getHtml(url)
    else:
        print(i, url, res.status_code, "{:.2f}".format(time.time() - start))
        i += 1

def getMHtml(url):
    global i
    try:
        start = time.time()
        res = requests.get(url, headers = headers, timeout=30)

        if res.status_code != 200:
            bad_url.append(str(url).replace("www", 'm'))
            # return getMHtml(url)

    except Exception as e:
        print(url, "异常", e)
        return getMHtml(url)

    else:
        print(i, str(url).replace("www", 'm'), res.status_code, "{:.2f}".format(time.time() - start))
        i += 1

def getList():
    try:
        res = requests.get(base_url)
        selector = html.fromstring(res.content)
    except:
        print("123")
    else:
        return [urllib.parse.urljoin(base_url, url) for url in selector.xpath("//div[@class='list-wenku']/div/a/@href")]



if __name__ == '__main__':
    # 多线程
    # strart = time.time()
    # pool = Pool(3)
    # pool.map(getHtml, getList())
    # print("{:.2f}".format(time.time() - strart))
    # 单线程
    strart = time.time()
    for info in getList():
        getHtml(info)
        print("{:.2f}".format(time.time() - strart))
    for info in getList():
        getMHtml(info)
        print("{:.2f}".format(time.time() - strart))
    print("{:.2f}".format(time.time() - strart))

    print("异常url：{}条".format(len(bad_url)))
    for i in bad_url:
        print(i)


