import re
from datetime import datetime
from collections import defaultdict
basetime = []


def getbasetime():
    for i in open("/Users/liye/Desktop/会计网日志分析/201709120001_www.kuaiji.com.access.log").readlines():

        has_ip = re.search(r'42.236.54.2 - - \[(.*?) \+0800\] "GET', i.strip())
        if has_ip:
            basetime.append(has_ip.group(1))


def transform_stamp(time_string):
    time_info = int(datetime.timestamp(datetime.strptime("{}".format(time_string), "%d/%b/%Y:%H:%M:%S")))
    # print(time_info)
    return time_info
def get_ip_count(ip_time_list):
    visit_count = 0
    # time_list = [int(datetime.timestamp(datetime.strptime("{}".format(i), "%d/%b/%Y:%H:%M:%S"))) for i in ip_time_list]
    for i in range(len(ip_time_list) - 1):
        b = ip_time_list[i+1] - ip_time_list[i]
        if b >= 1800:
            visit_count += 1
    return visit_count

def get_stay_time(ip_time_list):
    res = defaultdict(list)
    j = 0
    if len(ip_time_list) > 1:
        for i in range(len(ip_time_list) - 1):
            if ip_time_list[i + 1] - ip_time_list[i] > 1800:
                res[j].append(ip_time_list[i])
                j += 1
            else:
                res[j].append(ip_time_list[i])
        else:
            res[j].append(ip_time_list[i + 1])
    else:
        if ip_time_list:
            res[j].append(ip_time_list[0])
    # for k,v in res.items():
    #     print(max(v)-min(v),k, v)
    result = sum([max(v) - min(v) for k, v in res.items()])
    return result

if __name__ == '__main__':
    getbasetime()
    # for i in basetime:
    #     print(i)
    get_stay_time(sorted([transform_stamp(i) for i in basetime]))
