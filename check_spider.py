import re
import subprocess

from multiprocessing.dummy import Pool
baidu_macth_ip = []
other_ip = []
def getData(spiderlist):
    spider_info = subprocess.getoutput("nslookup {}".format(spiderlist))
    baidu_macth = re.match(r'.*?(baiduspider).*', spider_info, re.S)
    if baidu_macth:
        baidu_macth_ip.append(spiderlist)

        if spiderlist in set(other_ip):
            other_ip.remove(spiderlist)
    else:
        other_ip.append(spiderlist)
def run(all_spider_list):
    pool = Pool(50)
    pool.map(getData, list(set(all_spider_list)))

    [pool.map(getData, [i for i in set(other_ip)]) for _ in range(3)]

# if __name__ == '__main__':
    # start = datetime.now()
    # run([i for i in spider_list.split()])
    # print("符合百度蜘蛛的有：{}个".format(len(baidu_macth_ip)))
    # print("假百度蜘蛛有：{}个".format(len(set(other_ip))))
    # print("耗时：{}:{}".format((datetime.now()-start).seconds,(datetime.now()-start).microseconds))
# print("假IP列表")
# for i in set(other_ip):
#     print(i)
