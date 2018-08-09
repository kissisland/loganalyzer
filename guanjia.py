import requests, csv
from lxml import html
from multiprocessing.dummy import Pool

all_data = []
def getHtml(page_num):
    res = requests.get("http://www.zizhiguanjia.com/zs/pn{}".format(page_num))
    selector = html.fromstring(res.content)
    for info in selector.xpath("//div[@class='zsbase-r']/ul/li/div[@class='kn-time']/div"):
        title = info.xpath("a/text()")[0]
        link = info.xpath("a/@href")[0]
        tags = '|'.join(info.xpath("span[3]/a/text()"))
        all_data.append({
            'title' : title,
            'link' : link,
            'tags' : tags,
        })
        print(title, link, tags)

pool = Pool(10)
pool.map(getHtml, [i for i in range(1,622)])

writer = csv.DictWriter(f=open("guanjia.csv", 'w', newline='',encoding='utf-8'),fieldnames=['title','link','tags'])
writer.writerows(all_data)

