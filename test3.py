import requests,time
from lxml import html
from urllib.parse import urljoin
import csv, os, shutil, random

base_url = 'http://www.zhongzhu71.com/EnterpriseWikiType/EnterpriseWikiList'
login_url = 'http://www.zhongzhu71.com/WebBasUser/Login'

acount = 0
post_acount = 0

# from pymongo import MongoClient
# client = MongoClient()
# zhongzhu71 = client['zhongzhu71']
# news = zhongzhu71['news']
# file = open('zhongzhu71.csv', "w+", encoding='utf-8', newline='')
# writer = csv.DictWriter(file, fieldnames=["title", "link", "pushdate", "status", 'soulu'])
# writer.writeheader()
# for i in news.find({'status':1}):
#     writer.writerow({
#         "title":i['title'],
#         "link":i['link'],
#         "pushdate":i['pushdate'],
#         "status":i['status'],
#         'soulu':"暂未查询"
#     })
result_shou = []
def get_baidu_html(url):
    res = requests.get("http://www.baidu.com/s?word=%s"%url)
    htmldata = res.text
    if "很抱歉，没有找到与" in htmldata:
        # print(url, '未收录')
        return "未收录"
    elif "百度为您找到相关结果约" in htmldata and "没有找到该URL" not in htmldata:
        # print(url, '已收录')
        result_shou.append(url)
        return "已收录"
    elif "百度为您找到相关结果约" in htmldata and "没有找到该URL"  in htmldata:
        # print(url, "未收录")
        return "未收录"
    elif "http://verify.baidu.com" in htmldata:
        # print("出现验证码")
        time.sleep(1800)
        return get_baidu_html(url)
    else:
        # print("没有满足的条件")
        print(htmldata)
        return False
def update_status(link):
    for filename in ['zhongzhu71.csv', 'zhongzhu71.db']:
        data = []
        with open(filename, 'r+', encoding='utf-8')as f2:
            for r in csv.DictReader(f2):
                if r['link'] == link:
                    r['status'] = 1
                data.append(r)
        file = open(filename, "w", encoding='utf-8', newline='')
        writer = csv.DictWriter(file, fieldnames=["title", "link", "pushdate", "status", 'soulu'])
        writer.writeheader()
        writer.writerows(data)

def update_soulu(link,flag):
    for filename in ['zhongzhu71.csv', 'zhongzhu71.db']:
        data = []
        with open(filename, 'r', encoding='utf-8')as f1:
            for r in csv.DictReader(f1):
                if r['link'] == link and flag == "已收录":
                    r['soulu'] = "已收录"
                elif r['link'] == link and not flag == "未收录":
                    r['soulu'] = "未收录"
                else:
                    pass

                data.append(r)

        file = open(filename, "w", encoding='utf-8', newline='')
        writer = csv.DictWriter(file, fieldnames=["title", "link", "pushdate", "status", 'soulu'])
        writer.writeheader()
        writer.writerows(data)

def insert(dic):
    for filename in ['zhongzhu71.csv', 'zhongzhu71.db']:
        file = open(filename, "a", encoding='utf-8', newline='')
        writer = csv.DictWriter(file, fieldnames=["title", "link", "pushdate", "status", 'soulu'])
        writer.writerow(dic)

def loginZhongzhu():
    session = requests.session()
    res = session.post(login_url, data={"username":"李斌斌", 'password':"zz717171"})
    if "李斌斌" in res.text:
        print("网站登陆成功。。。。。" + '\n')
        return session
    else:
        print("登陆不成功，稍后重试...")

def postTobaidu(pushurl):
    res = requests.post("http://data.zz.baidu.com/urls?site=www.zhongzhu71.com&token=U8o6UylSS4Kw44Bt", data=pushurl)
    if res.json().get("success") == 1:
        return True
    else:
        return False

def getNewsList(login,url):
    res = login.get(url)
    seclect = html.fromstring(res.content)
    for item in seclect.xpath("//div[@class='bd']/table/tbody/tr"):
        title = item.xpath("td[@class='title']/text()")[0]
        link = str(item.xpath("td/@onclick")[0]).replace("window.location.href = '", '').replace("'", '')
        link = urljoin(base_url, link)
        pushdate = item.xpath("td[3]/text()")[0].split(" ")[0]

        file = open('zhongzhu71.db', 'r', encoding='utf-8')
        reader = csv.DictReader(file)
        if link in [r.get("link") for r in reader]:
            global acount
            acount += 1
            if acount == 5:
                break
        else:
            insert({
                "title": title,
                'link': link,
                'pushdate': pushdate,
                'status': 0,
                'soulu': "暂未查询"
            })
            if postTobaidu(link):
                global post_acount
                post_acount += 1
                print("{} 提交成功。".format(link))
                update_status(link)
    else:
        nextpage = seclect.xpath("//div[@class='pages']/a[@id='p_next']/@href")
        if nextpage:
            getNewsList(login, urljoin(base_url, nextpage[0]))

if __name__ == '__main__':
    # 抓取后台列表的文章信息并提交百度
    selector = input("""请选择你要操作的项目，按数字+回车确认：
1、把新发布的文章提交给百度。
2、如果误删或者误修改zhongzhu71.csv文件，按2恢复。
3、批量查询收录，并把查询结果写入zhongzhu71.csv文件

*文件中的zhongzhu71.db文件是数据库文件，切免删除。

>>>
""")
    if selector == '1':
        print("程序正在登陆中，请稍等~~~~~~~~~")
        lo = loginZhongzhu()
        getNewsList(lo, base_url)
        if post_acount == 0:
            print("没有新页面更新。")
        else:
            print(f"本次共提交链接：{post_acount}条")
    elif selector == '2':
        if os.path.exists('zhongzhu71.csv'):
            os.remove('zhongzhu71.csv')

        shutil.copyfile('zhongzhu71.db', 'zhongzhu71.csv')
        print('zhongzhu71.csv文件创建成功。')
    elif selector == "3":
        print("正在做收录查询：")
        re_data =[]
        all_art = 0
        key_num = 1
        with open("zhongzhu71.db", 'r', encoding='utf-8')as f:
            for l in csv.DictReader(f):
                if key_num % 10 == 0:
                    b = random.randint(2, 5)
                    time.sleep(b)
                ff = get_baidu_html(l['link'])
                key_num += 1
                l['soulu'] = ff
                re_data.append((l['link'], l['soulu']))
                all_art += 1
                print(l['link'], l['soulu'])
        for k,v in re_data:
            update_soulu(k, v)
        print("\n" + f"一共发了文章{all_art}篇，收录了：{len(result_shou)}篇文章了")

    time.sleep(120)
