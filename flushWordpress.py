import requests, random
from lxml import html
from multiprocessing.dummy import Pool
flush_like_url = 'https://www.paurl.com/wp-admin/admin-ajax.php'
urls = """
https://www.paurl.com/seo/345
https://www.paurl.com/seo/347
https://www.paurl.com/content/354
https://www.paurl.com/seo/367
"""
def flushReading(link):
    """
    根据wp的链接刷阅读量，可以根据随机数范围设定。
    """
    for _ in range(random.randrange(reading_start, reading_stop)):
        res = requests.get(link)
        selector = html.fromstring(res.content)
        read = selector.xpath("//div[@class='entry-info']/span[4]/text()")
        title = selector.xpath("//title/text()")
        print(title[0],read[0])

def flushLike(link):
    """
    根据wp的链接刷点赞量，可以根据随机数范围设定。
    """
    art_id = link.split("/")[-1]
    payload = {
        "action": "wpcom_like_it",
        "id": art_id
    }
    for _ in range(random.randrange(like_start, like_stop)):
        res = requests.post(flush_like_url, data=payload)
        print(res.content.decode())


pool = Pool(20)
reading_start = 1500
reading_stop = 1800
like_start = 80
like_stop = 120
# pool.map(flushReading, [k.strip() for k in urls.split()])
pool.map(flushLike, [k.strip() for k in urls.split()])
