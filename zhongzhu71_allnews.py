import requests
from lxml import html
from urllib.parse import urljoin
from pymongo import MongoClient

client = MongoClient()
zhongzhu71 = client['zhongzhu71']
news = zhongzhu71['news']

base_url = 'http://www.zhongzhu71.com/EnterpriseWikiType/EnterpriseWikiList'
login_url = 'http://www.zhongzhu71.com/WebBasUser/Login'

acount = 0
post_acount = 0

def chanStatus(link):
    news.update_one({'link':link},{"$set":{'status':1}})

def postTobaidu(pushurl):
    res = requests.post("http://data.zz.baidu.com/urls?site=www.zhongzhu71.com&token=U8o6UylSS4Kw44Bt", data=pushurl)
    if res.json().get("success") == 1:
        return True
    else:
        return False

def loginZhongzhu():
    session = requests.session()
    res = session.post(login_url, data={"username":"李斌斌", 'password':"zz717171"})
    if "李斌斌" in res.text:
        print("登陆成功。。。。。")
        return session
    else:
        print("登陆不成功，稍后重试...")

def getNewsList(login,url):
    res = login.get(url)
    seclect = html.fromstring(res.content)
    for item in seclect.xpath("//div[@class='bd']/table/tbody/tr"):
        title = item.xpath("td[@class='title']/text()")[0]
        link = str(item.xpath("td/@onclick")[0]).replace("window.location.href = '", '').replace("'", '')
        link = urljoin(base_url, link)
        pushdate = item.xpath("td[3]/text()")[0].split(" ")[0]
        if news.find_one({'link': link}):
            global acount
            acount += 1
            if acount == 5:
                break
        else:
            news.insert_one({
                "title": title,
                'link': link,
                'pushdate': pushdate,
                'status': 0
            })
            if postTobaidu(link):
                global post_acount
                post_acount += 1
                print("{} 提交成功。".format(link))
                chanStatus(link)
    else:
        nextpage = seclect.xpath("//div[@class='pages']/a[@id='p_next']/@href")
        if nextpage:
            getNewsList(login, urljoin(base_url, nextpage[0]))

# 把没有推送的链接推送，并修改状态为1（已提交）
def showNoprintNews():
    for i in news.find({"status":0}):
        if postTobaidu(i['link']):
            print("{} 推送成功".format(i['link']))
            chanStatus(i['link'])

def showNews():
    return [i['link'] for i in news.find()]

if __name__ == '__main__':
    # 抓取后台列表的文章信息并提交百度
    login = loginZhongzhu()
    getNewsList(login,base_url)
    if post_acount == 0:
        print("没有新页面更新。")
    else:
        print("共提交链接：{}条".format(post_acount))


    # 查询全部链接
    # for i in showNews():
    #     print(i)

    # 查询全部链接并按每500条分组
    # all_links = [i for i in showNews()]
    # all_links_group = []
    # for i in range(0, len(all_links), 500):
    #     all_links_group.append(all_links[i:i+500])
    #
    # for k,v in enumerate(all_links_group):
    #     print("第{}组数据:".format(k+1))
    #     for i in v:
    #         print(i)
    #     print("第{}组共{}条链接完毕>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(k+1, len(v)), '\n')
