import re,datetime,csv
from multiprocessing.dummy import Pool
import testtime2
from collections import Counter
from check_spider import other_ip,baidu_macth_ip,run
from urllib.parse import urljoin
import readlogfile
"""
Baiduspider，360spider，Sogou web spider
光年统计计算方式：
访问次数：该IP从第一次访问到离开时间在1800秒内，算一次访问
访问时间：各IP每次抓取时间段和
访问总量：抓取条数
"""

def save_file(dict_list,whatfile,filename,field_list):
    file = open(r'E:\会计网日志分析\{}_{}.csv'.format(whatfile,filename), 'a+', newline='')
    # field_list = ['date','baidu_visit','baidu_stay_time(h)','baidu_no_repeat','baidu_404','so_visit','so_stay_time(h)','so_no_repeat','so_404','sougou_visit','sougou_stay_time(h)','sougou_no_repeat','sougou_404']
    writer = csv.DictWriter(file, fieldnames=field_list)
    # writer.writeheader()
    writer.writerow(dict_list)
    file.close()

def getAnalyzer(textline):
    # 把蜘蛛访问日志提取出来
    # spider_data = re.search(r'.*?(Baiduspider|360Spider|Sogou web spider).*"', textline)
    baiduMatch = re.match(r'.*?Baiduspider.*"', textline[1])
    soMatch = re.match(r'.*?360Spider.*"', textline[1])
    sougouMatch = re.match(r'.*?(Sogou web spider).*"', textline[1])

    if baiduMatch:
        # 总的百度IP抓取量
        baidu_all_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', baiduMatch.group()).group())

        # 时间段的抓取量
        baidu_time_scrapy.append(re.search(r'\d+:(\d+):\d', textline[1]).group(1))

        # 不重复抓取的量
        baidu_no_repeat_links.append(textline[1].split()[6])

        # 总访问时间
        baidu_visit = re.match(r'(\d+.\d+.\d+.\d+) - - \[(.*?) \+0800\] "GET', baiduMatch.group())
        if baidu_visit:
            baidu_visit_list.append({baidu_visit.group(1): baidu_visit.group(2)})

        # 状态码
        baidu_status_code.append(textline[1].split()[8])

        # 404的页面数据
        if_404 = re.search(r'".*? (.*?) HTTP/1.1" 404.*', baiduMatch.group())
        if if_404:
            baidu_links_404.append(if_404.group(1))

        # 500的页面数据
        if_500 = re.search(r'".*? (.*?) HTTP/1.1" 500.*', baiduMatch.group())
        if if_500:
            baidu_links_500.append(if_500.group(1))

        # 每个目录的抓取量
        dir_scrapy = re.search(r'".*? (.*?) HTTP/1.1"', baiduMatch.group())
        if dir_scrapy:
            is_dir_scrapy = re.search(r'/(.*?/|$)', dir_scrapy.group(1))
            if is_dir_scrapy:
                baidu_dir_scrapy.append(is_dir_scrapy.group())
                # print(re.search(r'/(.*?/|$)', dir_scrapy.group(1)).group())

        # IP的抓取量
        # baidu_ip_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', textline[1]).group())
        # 哪些文章被抓了
        # baidu_find_article.append(re.search(r'/.*?/(\d+){7}', textline[1].split()[6]).group(1))
        # if re.search(r'/.*?/(\d{7})', textline[1].split()[6]):
        #     baidu_find_article.append(re.search(r'/.*?/(\d{7})', textline[1].split()[6]).group(1))
    elif soMatch:
        # 总访问量
        so_all_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', soMatch.group()).group())

        # 时间段的抓取量
        so_time_scrapy.append(re.search(r'\d+:(\d+):\d', textline[1]).group(1))

        # 不重复抓取的量
        so_no_repeat_links.append(textline[1].split()[6])

        # 总访问时间
        so_visit = re.match(r'(\d+.\d+.\d+.\d+) - - \[(.*?) \+0800\] "GET', soMatch.group())
        if so_visit:
            so_visit_list.append({so_visit.group(1): so_visit.group(2)})

        # 状态码
        so_status_code.append(textline[1].split()[8])

        # 404的页面数据
        if_404 = re.search(r'".*? (.*?) HTTP/1.1" 404.*', soMatch.group())
        if if_404:
            so_links_404.append(if_404.group(1))

        # 500的页面数据
        if_500 = re.search(r'".*? (.*?) HTTP/1.1" 500.*', soMatch.group())
        if if_500:
            so_links_500.append(if_500.group(1))

        # 每个目录的抓取量
        dir_scrapy = re.search(r'".*? (.*?) HTTP/1.1"', soMatch.group())
        if dir_scrapy:
            is_dir_scrapy = re.search(r'/(.*?/|$)', dir_scrapy.group(1))
            if is_dir_scrapy:
                so_dir_scrapy.append(is_dir_scrapy.group())

        # IP的抓取量
        # so_ip_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', textline[1]).group())

    elif sougouMatch:
        # 总访问量
        sougou_all_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', sougouMatch.group()).group())

        # 时间段的抓取量
        sougou_time_scrapy.append(re.search(r'\d+:(\d+):\d', textline[1]).group(1))

        # 不重复抓取的量
        sougou_no_repeat_links.append(textline[1].split()[6])

        # 总访问时间
        sougou_visit = re.match(r'(\d+.\d+.\d+.\d+) - - \[(.*?) \+0800\] "GET', sougouMatch.group())
        if sougou_visit:
            sougou_visit_list.append({sougou_visit.group(1): sougou_visit.group(2)})

        # 状态码
        sougou_status_code.append(textline[1].split()[8])

        # 404的页面数据
        if_404 = re.search(r'".*? (.*?) HTTP/1.1" 404.*', sougouMatch.group())
        if if_404:
            sougou_links_404.append(if_404.group(1))

        # 500的页面数据
        if_500 = re.search(r'".*? (.*?) HTTP/1.1" 500.*', sougouMatch.group())
        if if_500:
            sougou_links_500.append(if_500.group(1))

        # 每个目录的抓取量
        dir_scrapy = re.search(r'".*? (.*?) HTTP/1.1"', sougouMatch.group())
        if dir_scrapy:
            if 'www' in general_file:
                is_dir_scrapy = re.search(r'/(.*?/|$)', dir_scrapy.group(1))
                if is_dir_scrapy:
                    sougou_dir_scrapy.append(is_dir_scrapy.group())
            elif general_file.startswith('m'):
                is_dir_scrapy = re.search(r'/(.*?/|$)', dir_scrapy.group(1))
                if is_dir_scrapy:
                    sougou_dir_scrapy.append(is_dir_scrapy.group())

        # IP的抓取量
        # sougou_ip_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', textline[1]).group())

    # IP的抓取量
    # ip_scrapy.append(re.search(r'(\d+).(\d+).(\d+).(\d+)', textline[1]).group())

    # 404的页面有哪些
    # if textline[1].split()[8] == "404":
    #     links_404.append(textline[1].split()[6])

# 总访问数
def getVisit(spider_all_ip,visit_list):
    visit_dict = {}
    for i in set(spider_all_ip):
        visit_dict[i] = []

    [visit_dict[k].append(testtime2.transform_stamp(v)) for i in visit_list for k, v in i.items() if k in visit_dict.keys()]
    return visit_dict




# 状态码统计
def getStatus(baidu_status,so_status,sougou_status):
    for item_index,item_list in enumerate([baidu_status,so_status,sougou_status]):
        # if item_index == 0:
        #     info_output.write("百度状态码统计："+ '\n')
        # elif item_index == 1:
        #     info_output.write("360状态码统计："+ '\n')
        # elif item_index == 2:
        #     info_output.write("搜狗状态码统计："+ '\n')
        info_output.write(str(item_list.count("404"))+ '\n')
        info_output.write(str(item_list.count("302"))+ '\n')
        info_output.write(str(item_list.count("301"))+ '\n')
        info_output.write(str(item_list.count("403"))+ '\n')
        info_output.write(str(item_list.count("200"))+ '\n')
        info_output.write(str(item_list.count("405"))+ '\n')
        info_output.write(str(item_list.count("500"))+ '\n')
        info_output.write(str(item_list.count("499"))+ '\n')
        info_output.write(str(item_list.count("502"))+ '\n')

        info_output.write('\n\n')

# 时间段抓取
def getTimeCrawl(baidu_time,so_time,sougou_time):
    # info_output.write("百度时间抓取" + '\n')
    for i in range(24):
        # print("{:0>2}点百度抓取量：{}".format(i, baidu_time.count("{:0>2}".format(i))))
        info_output.write('{}'.format(baidu_time.count("{:0>2}".format(i))) + '\n')
    else:
        info_output.write('\n\n')

    # info_output.write("360时间抓取" + '\n')
    for i in range(24):
        info_output.write('{}'.format(so_time.count("{:0>2}".format(i))) + '\n')
    else:
        info_output.write('\n\n')

    # info_output.write("搜狗时间抓取" + '\n')
    for i in range(24):
        info_output.write('{}'.format(sougou_time.count("{:0>2}".format(i))) + '\n')

# 各IP抓取量
# print("百度IP抓取top10")
# for k,v in sorted(Counter(baidu_all_scrapy).items(), key=lambda x:x[1],reverse=True)[:10]:
#     print("{}抓取了：{}".format(k, v))
def getIpCount(baidu_ip,so_ip,sougou_ip):
    # info_output.write("百度ip抓取：" + '\n')
    # for k,v in sorted({ip_duan_no:sum([str(item).startswith(ip_duan_no) for item in baidu_ip]) for ip_duan_no in set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(baidu_ip)])}.items(), key=lambda x:x[1],reverse=True):
    #     info_output.write("{} {}".format(k, v) + '\n')
    baidu_ip_dict = {ip_duan_no: sum([str(item).startswith(ip_duan_no) for item in baidu_ip]) for ip_duan_no in set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(baidu_ip)])}
    info_output.write(str(baidu_ip_dict.get("123.125.71", 0)) + '\n')
    info_output.write(str(baidu_ip_dict.get("220.181.108", 0)) + '\n')
    info_output.write(str(baidu_ip_dict.get("111.206.221", 0)) + '\n')
    info_output.write(str(baidu_ip_dict.get("180.76.15", 0)) + '\n')


    # info_output.write("360ip抓取：" + '\n')
    # for k, v in sorted({ip_duan_no: sum([str(item).startswith(ip_duan_no) for item in so_ip]) for ip_duan_no in
    #                     set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(so_ip)])}.items(),
    #                    key=lambda x: x[1], reverse=True):
    #     info_output.write("{} {}".format(k, v) + '\n')
    so_ip_dict = {ip_duan_no: sum([str(item).startswith(ip_duan_no) for item in so_ip]) for ip_duan_no in
                        set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(so_ip)])}
    info_output.write(str(so_ip_dict.get("42.236.99", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.48", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.49", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("180.153.236", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.10", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.12", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.54", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.101", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.102", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.46", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.55", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.103", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("180.153.232", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("180.153.234", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.48", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.49", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("182.118.61", 0)) + '\n')
    info_output.write(str(so_ip_dict.get("42.236.50", 0)) + '\n')


    # info_output.write("搜狗ip抓取：" + '\n')
    # for k, v in sorted({ip_duan_no: sum([str(item).startswith(ip_duan_no) for item in sougou_ip]) for ip_duan_no in
    #                     set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(sougou_ip)])}.items(),
    #                    key=lambda x: x[1], reverse=True):
    #     info_output.write("{} {}".format(k, v) + '\n')

    sougou_ip_dict = {ip_duan_no: sum([str(item).startswith(ip_duan_no) for item in sougou_ip]) for ip_duan_no in
                        set([re.search(r'\d+\.\d+\.\d+', i).group() for i in set(sougou_ip)])}
    info_output.write(str(sougou_ip_dict.get("106.38.241", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("123.126.113", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("106.120.173", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("123.126.68", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("218.30.103", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("220.181.124", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("36.110.147", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("123.125.125", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("183.36.114", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("58.250.125", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("111.202.102", 0)) + '\n')
    info_output.write(str(sougou_ip_dict.get("106.120.188", 0)) + '\n')

# 404的页面有哪些
def dir404_crawl(baidu_404_list,so_404_list,sougou_404_list):
    for i_index,i_info in enumerate([baidu_404_list,so_404_list,sougou_404_list]):
        if i_index == 0:
            output_404.write("百度 404页面" + '\n')
        elif i_index == 1:
            output_404.write("360 404页面" + '\n')
        elif i_index == 2:
            output_404.write("搜狗 404页面" + '\n')

        for i in i_info:
            output_404.write(i + '\n')
        else:
            output_404.write("\n")

# 500的页面有哪些
def dir500_crawl(baidu_500_list, so_500_list, sougou_500_list):
    list500 = []
    list500.extend(baidu_500_list)
    list500.extend(so_500_list)
    list500.extend(sougou_500_list)
    host_url = 'http://www.kuaiji.com'
    for i in list500:
        output_500.write(urljoin(host_url, i) + '\n')
    else:
        output_500.write("\n")

# 各目录抓取量是多少
def dir_crawl_allcount(baidudirscrapy,sodirscrapy,sougoudirscrapy):
    for i_index, i_info in enumerate([baidudirscrapy,sodirscrapy,sougoudirscrapy]):
        if i_index == 0:
            output_dir_count.write("百度 目录抓取统计：" + '\n')
        elif i_index == 1:
            output_dir_count.write("360 目录抓取统计：" + '\n')
        elif i_index == 2:
            output_dir_count.write("搜狗 目录抓取统计：" + '\n')

        for k,v in sorted(Counter(i_info).items(), key=lambda x:x[1], reverse=True):
            output_dir_count.write("{}抓取量：{}".format(k, v) + "\n")
        else:
            output_dir_count.write("\n")


def dir_crawl(baidu_dir, so_dir, sougou_dir):
    for item_index,item_info in enumerate([baidu_dir, so_dir, sougou_dir]):
        # if item_index == 0:
        #     info_output.write("百度目录抓取量" + '\n')
        # elif item_index == 1:
        #     info_output.write("360目录抓取量" + '\n')
        # elif item_index == 2:
        #     info_output.write("搜狗目录抓取量" + '\n')
        info_output.write(str(Counter(item_info).get("/")) + '\t')
        info_output.write(str(Counter(item_info).get("/news/")) + '\t')
        info_output.write(str(Counter(item_info).get("/weixin/")) + '\t')
        info_output.write(str(Counter(item_info).get("/shiwu/")) + '\t')
        info_output.write(str(Counter(item_info).get("/fagui/")) + '\t')
        info_output.write(str(Counter(item_info).get("/wenxuan/")) + '\t')
        info_output.write(str(Counter(item_info).get("/xuexiao/")) + '\t')
        info_output.write(str(Counter(item_info).get("/kecheng/")) + '\t')
        info_output.write(str(Counter(item_info).get("/peixun/")) + '\t')
        info_output.write(str(Counter(item_info).get("/exam/")) + '\t\t')
    info_output.write('\n')

input_name = readlogfile.readLogfile()
print("日志分析工作正在开始......")
print("需要分析：{}".format(','.join(input_name)))
starttime = datetime.datetime.now()
for in_name in input_name:
    status_code = []

    sougo_no_repeat_links = []
    baidu_time_scrapy = []
    sougo_time_scrapy = []
    ip_scrapy = []

    so_all_scrapy = []
    sougou_all_scrapy = []
    baidu_find_article = []
    baidu_stop_time = []
    baidu_all_stopseconds = 0

    baidu_no_repeat_links = []
    baidu_all_scrapy = []
    baidu_links_404 = []
    baidu_dir_scrapy = []
    baidu_status_code = []
    baidu_visit_list = []

    so_no_repeat_links = []
    so_time_scrapy = []
    so_visit_list = []
    so_dir_scrapy = []
    so_links_404 = []
    so_status_code = []

    sougou_no_repeat_links = []
    sougou_time_scrapy = []
    sougou_visit_list = []
    sougou_dir_scrapy = []
    sougou_links_404 = []
    sougou_status_code = []

    baidu_links_500 = []
    so_links_500 = []
    sougou_links_500 = []

    file_data = open("E:\会计网日志分析\{}.log".format(in_name))
    pool = Pool(100)

    file_name = file_data.name
    file_create_date = re.search(r'(\d){8}',file_name).group()
    general_file = re.search(r'_(\w+\.kuaiji\.com)', file_name.split("/")[-1]).group(1).replace('.','')
    pool.map(getAnalyzer, enumerate([i.strip() for i in file_data.readlines()]))
    info_output =  open(r"E:\会计网日志分析\info_output.txt",'a')
    output_404 =  open(r"E:\会计网日志分析\详情输出\404_output_{}.txt".format(file_create_date), 'w')
    output_500 =  open(r"E:\会计网日志分析\详情输出\500_output_{}.txt".format(file_create_date), 'w')
    output_dir_count =  open(r"E:\会计网日志分析\详情输出\dir_output_{}.txt".format(file_create_date), 'w')

    # IP验证
    run(baidu_all_scrapy)
    baidu_ip_check = baidu_macth_ip
    baidu_ip_other = other_ip

    baidu_visit_count = sum([testtime2.get_ip_count(sorted(v)) for k,v in getVisit(baidu_ip_check, baidu_visit_list).items()])
    so_visit_count = sum([testtime2.get_ip_count(sorted(v)) for k,v in getVisit(so_all_scrapy, so_visit_list).items()])
    sougou_visit_count = sum([testtime2.get_ip_count(sorted(v)) for k,v in getVisit(sougou_all_scrapy, sougou_visit_list).items()])
    baidu_fake_visit_count = sum([testtime2.get_ip_count(sorted(v)) for k,v in getVisit(baidu_ip_other, baidu_visit_list).items()])
    print("百度总访问量是：{}".format(baidu_visit_count))
    print("百度假IP总访问量是：{}".format(baidu_fake_visit_count))
    print("360总访问量是：{}".format(so_visit_count))
    print("搜狗总访问量是：{}".format(sougou_visit_count))

    # 总停留时间
    baidu_stay_time = round(sum([testtime2.get_stay_time(sorted(v)) for k,v in getVisit(baidu_macth_ip, baidu_visit_list).items()])/3600,2)
    so_stay_time = round(sum([testtime2.get_stay_time(sorted(v)) for k,v in getVisit(so_all_scrapy, so_visit_list).items()])/3600,2)
    sougou_stay_time = round(sum([testtime2.get_stay_time(sorted(v)) for k,v in getVisit(sougou_all_scrapy, sougou_visit_list).items()])/3600,2)

    print("百度总停留时间（小时）：{}".format(baidu_stay_time))
    print("360总停留时间（小时）：{}".format(so_stay_time))
    print("搜狗总停留时间（小时）：{}".format(sougou_stay_time))



    # 蜘蛛数量统计
    # baidu_scrapy_count = len(set(baidu_all_scrapy))
    so_scrapy_count = len(set(so_all_scrapy))
    sougou_scrapy_count = len(set(sougou_all_scrapy))

    # print("百度总抓取量：{}".format(baidu_scrapy_count))
    print("百度真蜘蛛数：{}".format(len(set(baidu_ip_check))))
    print("百度假蜘蛛数：{}".format(len(set(baidu_ip_other))))
    print("360真蜘蛛数：{}".format(so_scrapy_count))
    print("搜狗真蜘蛛数：{}".format(sougou_scrapy_count))

    # 不重复抓取的量
    baidu_no_repeat = len(set(baidu_no_repeat_links))
    so_no_repeat = len(set(so_no_repeat_links))
    sougou_no_repeat = len(set(sougou_no_repeat_links))

    print("百度不重复抓取的数量是：{}".format(baidu_no_repeat))
    print("360不重复抓取的数量是：{}".format(so_no_repeat))
    print("搜狗不重复抓取的数量是：{}".format(sougou_no_repeat))

    # 总抓取的量
    baidu_sum = len(baidu_no_repeat_links)
    so_sum = len(so_no_repeat_links)
    sougou_sum = len(sougou_no_repeat_links)
    print("百度总抓取的数量是：{}".format(baidu_sum))
    print("360总抓取的数量是：{}".format(so_sum))
    print("搜狗总抓取的数量是：{}".format(sougou_sum))

    # 404有多少
    baidu_404 = len(baidu_links_404)
    so_404 = len(so_links_404)
    sougou_404 = len(sougou_links_404)



    baidu_news_all_scrapy = [x for x in baidu_all_scrapy if x not in other_ip]

    info_output.write("{},{}".format(file_create_date,general_file) + '\n')
    info_output.write("搜索引擎目录抓取统计" + '\n')
    dir_crawl(baidu_dir_scrapy,so_dir_scrapy,sougou_dir_scrapy)
    info_output.write("时间抓取统计" + '\n')
    getTimeCrawl(baidu_time_scrapy,so_time_scrapy,sougou_time_scrapy)
    info_output.write("状态码" + '\n')
    getStatus(baidu_status_code,so_status_code,sougou_status_code)
    info_output.write("ip抓取：" + '\n')
    getIpCount(baidu_news_all_scrapy, so_all_scrapy, sougou_all_scrapy)
    info_output.close()
    save_file({
        "date":file_create_date,
        "baidu_visit":baidu_visit_count,
        "baidu_stay_time(h)":baidu_stay_time,
        "baidu_sum":baidu_sum,
        "baidu_no_repeat":baidu_no_repeat,
        "baidu_spider_count":len(set(baidu_ip_check)),
        "baidu_fake_spider":len(set(baidu_ip_other)),
        # 'baidu_404':baidu_404,
        "so_visit":so_visit_count,
        "so_stay_time(h)":so_stay_time,
        'so_sum':so_sum,
        "so_no_repeat":so_no_repeat,
        "so_spider_count":so_scrapy_count,
        # 'so_404':so_404,
        "sougou_visit":sougou_visit_count,
        "sougou_stay_time(h)":sougou_stay_time,
        'sougou_sum':sougou_sum,
        "sougou_no_repeat":sougou_no_repeat,
        "sougou_spider_count":sougou_scrapy_count,
        # 'sougou_404':sougou_404,
    },general_file,"general",['date','baidu_visit','baidu_stay_time(h)',"baidu_sum",'baidu_no_repeat',"baidu_spider_count",'baidu_fake_spider','so_visit','so_stay_time(h)','so_sum','so_no_repeat',"so_spider_count",'sougou_visit','sougou_stay_time(h)','sougou_sum','sougou_no_repeat',"sougou_spider_count"])

    # 把404页面单独保存出来
    dir404_crawl(baidu_links_404,so_links_404,sougou_links_404)
    output_404.close()

    # 把500页面单独保存出来
    dir500_crawl(baidu_links_500,so_links_500,sougou_links_500)
    output_500.close()

    # 把各目录抓取量单独保存出来
    dir_crawl_allcount(baidu_dir_scrapy,so_dir_scrapy,sougou_dir_scrapy)
    output_dir_count.close()

    other_ip.clear()
    baidu_macth_ip.clear()

readlogfile.writeLogfile()
print(round((datetime.datetime.now()-starttime).seconds / 60,2))
