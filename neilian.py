import requests, csv

base_url = 'http://qeqiyx.kuaiji.com/?app=system&controller=keylink&action=page&orderby=weight%7Cdesc,id%7Cdesc&pagesize=1402'
add_url = 'http://qeqiyx.kuaiji.com/?app=system&controller=keylink&action=add'
headers = {
    'Accept':'application/json, text/javascript, */*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control':'no-cache',
    'Cookie':'UM_distinctid=15f05d24a5f258-0f235206086e1e-3b3e5906-13c680-15f05d24a60953; CT_ce17_ulastactivity=1494296600%7C0; CT_ce17_smile=1D1; CT_ce17_connect_is_bind=0; _qddaz=QD.tiyry4.s3nvtz.j8ntjejo; pgv_pvi=670085472; CT_rememberusername=yejh; _ga=GA1.2.489213324.1507705151; KJ_city_str=440100%7C%E5%B9%BF%E5%B7%9E%7Cguangzhou; KJ_city_id=440100; KJ_city_py=guangzhou; KJ_city=mwAJAEsAAABIABEAXQAWACUAEgBeAAYATAABADUAQQBDAFYADAAOABgAGgA2AAYAGgAaAAAAFQAWAAYAGQBBAFUAVgBZAFMASQBEAF0AVwBbAE4ASwAHABAAKwAMAAAAFwAdAB8ADAALAAQASwBPAFsADgAOAEEAQwBWAB0AEQAWABwAGgBBAFUAVgAcAAwAEQAOAA4ADQAYAAEADgBBAEMAVgAHAAoAAAAaAAAAEwBbAFgASwAGAB0AEABcABYAJQASAF4ABgBMAAEANQBBAEMAVgAaAAIAEAAYAAgAQQBVAFYAWwBTABwAQQAcAD8AHAAQAA0AVgAMACgADwBUABwAQQAcAD8AWwBOAEsABgAVAAAAAAAXAFsAWABLAFMASQBFAFkAVwBNAFYAUwBBAB0AHQBLABgA; PHPSESSID=gur00714orvgnl8ibkhsmv8ng2; CT_auth=DgBXAG0ADAAZAAQAHgBvAFEAVgBLAFUAVwBUAFEA; CT_userid=5204825; CT_username=yejh; _gid=GA1.2.2126794779.1517194224; Hm_lvt_6351a3b7008dd579cbc50ffbebf7267a=1516848857,1516956657,1516956797,1517215476; Hm_lvt_5bae5f8e67735251973fbd5cec28e2d0=1516848857,1516956656,1516956797,1517215477; Hm_lpvt_5bae5f8e67735251973fbd5cec28e2d0=1517215477; kj_session=eyJpdiI6ImxqcCtrWXNYVlJnWVJMQ0dVTGVTN2c9PSIsInZhbHVlIjoiV216THByWlJ4bkVYUnNNbEl6cXZyWUw1TEd2c0E0T0Z1dm9QSUlWNHFhN2NiVTJ1NURSb0dJTlN5TWg2XC9RNjJGU2NnUll0OEhDOHpaM3hiK2Z1Z0h3PT0iLCJtYWMiOiI4ODgxZjRkMDkxYTIyNTM4ZDVjMzBiMWNhMTU4OGE2YWY0OGE2YTdkMTc0Y2UyZjZjN2RkNmQ2YzljNTk5MGVhIn0%3D; sso_token_broker=efknuh9eqy0okcc0wkwc0sskc; Hm_lpvt_6351a3b7008dd579cbc50ffbebf7267a=1517296615',
    'Host':'qeqiyx.kuaiji.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://qeqiyx.kuaiji.com/?app=system&controller=keylink&action=index',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

def addData():
    pyload = {
        'name': '会计网2',
        'url': 'http://www.kuaiji.com',
    }
    res = requests.post(add_url, headers=headers, data=pyload)
    if res.json().get("state"):
        post_id = res.json().get("data").get("id")
        pyload2 = {
            'id' : post_id,
            'weight' : 800
        }
        requests.post('http://qeqiyx.kuaiji.com/?app=kuaiji&controller=keylink&action=set_weight', headers=headers, data=pyload2)

def getData():
    all_data = []
    res = requests.get(base_url, headers=headers)
    data = res.json()
    for info in data['data']:
        all_data.append(info)
    return all_data
def save(data):
    file = open('neilian.csv','w',encoding='GBK', newline='')
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    file.close()
# 保存所有内链信息到csv
# save(getData())

addData()