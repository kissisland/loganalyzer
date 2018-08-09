import requests, time

# start_url = "http://qeqiyx.kuaiji.com/?app=article&controller=article&action=remove&contentid={}"
#
# headers = {
#     'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
#     "Cookie" : "UM_distinctid=1646da430a1478-0dd8b355a02b1a-3c3c5d0c-13c680-1646da430a2817; _ga=GA1.2.2141903969.1530847834; _qddaz=QD.v5nuep.9gmiyr.jj9fa312; CT_rememberusername=yejh; CT_ce17_saltkey=O8e4uH8u; CT_ce17_lastvisit=1532594356; CT_ce17_atarget=1; pgv_pvi=3020980496; Hm_lvt_5bae5f8e67735251973fbd5cec28e2d0=1530847835,1532597504,1533020405; KJ_city_str=440100%7C%E5%B9%BF%E5%B7%9E%7Cguangzhou; KJ_city_id=440100; KJ_city_py=guangzhou; KJ_city=hgAUAEEAGgBFAAwAVwAMACgADwBUABwAQQAcAD8AWwBOAEsABgAUABUABwA8ABwAFwAHAAoADwAbABsAEwBbAFgASwBTAEkARABZAFcATQBWAFMAQQAdAB0ANgAGABoAGgAAABUAFgAGABkAQQBVAFYAHAAMABEADgAOAA0AGAABAA4AQQBDAFYABwAKAAAAGgAAABMAWwBYAEsABgAdABAAXAAWACUAEgBeAAYATAABADUAQQBDAFYAGgACABAAGAAIAEEAVQBWAAwABwAdAEEAHAA%2FAB8AQwAMAFYADAAoAEsAWQBbABEABQAXABAAAABLAE8ASQBEAFgAUwBNAEAAUwBBAB0AHQBLABgA; pgv_info=ssi=s2184128172; Hm_lvt_6351a3b7008dd579cbc50ffbebf7267a=1532597504,1533003451,1533541515; CT_ce17_st_p=0%7C1533541517%7Cc2348f138df5941e53f49be17fe8f980; CT_ce17_visitedfid=606; CT_ce17_viewid=tid_2423; Hm_lpvt_6351a3b7008dd579cbc50ffbebf7267a=1533541527; CT_ce17_lastact=1533546613%09forum.php%09guide; PHPSESSID=g6otcoii57uut6ev9j9d2n3dh7; CT_auth=DgBXAG0ADAAZAAQAHgBvAFEAVgBLAFUAVwBUAFEA; CT_userid=5204825; CT_username=yejh"
# }
#
# for i in ids.split():
#
#     res = requests.get(start_url.format(i), headers = headers)
#     data = res.json()
#     if data.get("state"):
#         print(f"{start_url.format(i)}删除成功了")
#         time.sleep(1)

res = requests.get("https://www.paurl.com")
print(res.text)