import requests, time
from lxml import html
base_url = 'http://ask.rednet.cn/explore/ajax/list/sort_type-new__topic_id-997__page-{}'
def getData(page):
    res = requests.get(base_url.format(page))
    res.encoding = res.apparent_encoding
    if len(res.text):
        selector = html.fromstring(res.text)
        titles = selector.xpath("//div[@class='aw-question-content']/h4/a/text()")
        # print(titles)
        print(len(titles), page)

        # for title in titles:
        #     with open('shuiwutitle.txt', 'a',encoding='utf-8')as f:
        #         f.write(title.strip() + '\n')
        # time.sleep(1)
        return True
    else:
        return False

for i in range(1,50):
    if getData(i):
        pass
    else:
        break
