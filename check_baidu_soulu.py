import requests, time, random
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"}

result_shou = list()
def get_baidu_html(url):
    res = requests.get("http://www.baidu.com/s?word=%s"%url)
    html = res.text
    if "很抱歉，没有找到与" in html:
        print(url, '未收录')
        return 1
    elif "百度为您找到相关结果约" in html and "没有找到该URL" not in html:
        print(url, '已收录')
        result_shou.append(url)
        return 0
    elif "http://verify.baidu.com" in html:
        print("出现验证码")
        time.sleep(1800)
        return

urls = """
http://www.zhongzhu71.com/detail/177.html
http://www.zhongzhu71.com/detail/176.html
http://www.zhongzhu71.com/detail/175.html
http://www.zhongzhu71.com/detail/174.html
http://www.zhongzhu71.com/detail/173.html
http://www.zhongzhu71.com/detail/172.html
http://www.zhongzhu71.com/detail/171.html
http://www.zhongzhu71.com/detail/170.html
http://www.zhongzhu71.com/detail/169.html
http://www.zhongzhu71.com/detail/168.html
http://www.zhongzhu71.com/detail/167.html
http://www.zhongzhu71.com/detail/166.html
http://www.zhongzhu71.com/detail/165.html
http://www.zhongzhu71.com/detail/164.html
http://www.zhongzhu71.com/detail/163.html
http://www.zhongzhu71.com/detail/162.html
http://www.zhongzhu71.com/detail/161.html
http://www.zhongzhu71.com/detail/160.html
http://www.zhongzhu71.com/detail/159.html
http://www.zhongzhu71.com/detail/158.html
http://www.zhongzhu71.com/detail/157.html
http://www.zhongzhu71.com/detail/156.html
http://www.zhongzhu71.com/detail/155.html
http://www.zhongzhu71.com/detail/154.html
http://www.zhongzhu71.com/detail/153.html
http://www.zhongzhu71.com/detail/152.html
http://www.zhongzhu71.com/detail/151.html
http://www.zhongzhu71.com/detail/150.html
http://www.zhongzhu71.com/detail/149.html
http://www.zhongzhu71.com/detail/148.html
http://www.zhongzhu71.com/detail/147.html
http://www.zhongzhu71.com/detail/146.html
http://www.zhongzhu71.com/detail/145.html
http://www.zhongzhu71.com/detail/144.html
http://www.zhongzhu71.com/detail/143.html
http://www.zhongzhu71.com/detail/142.html
http://www.zhongzhu71.com/detail/141.html
http://www.zhongzhu71.com/detail/140.html
http://www.zhongzhu71.com/detail/139.html
http://www.zhongzhu71.com/detail/138.html
http://www.zhongzhu71.com/detail/136.html
http://www.zhongzhu71.com/detail/135.html
http://www.zhongzhu71.com/detail/134.html
http://www.zhongzhu71.com/detail/132.html
http://www.zhongzhu71.com/detail/131.html
http://www.zhongzhu71.com/detail/130.html
http://www.zhongzhu71.com/detail/122.html
http://www.zhongzhu71.com/detail/119.html
http://www.zhongzhu71.com/detail/118.html
http://www.zhongzhu71.com/detail/117.html
http://www.zhongzhu71.com/detail/116.html
http://www.zhongzhu71.com/detail/115.html
http://www.zhongzhu71.com/detail/114.html
http://www.zhongzhu71.com/detail/113.html
http://www.zhongzhu71.com/detail/112.html
http://www.zhongzhu71.com/detail/111.html
http://www.zhongzhu71.com/detail/109.html
http://www.zhongzhu71.com/detail/108.html
http://www.zhongzhu71.com/detail/107.html
http://www.zhongzhu71.com/detail/106.html
http://www.zhongzhu71.com/detail/105.html
http://www.zhongzhu71.com/detail/104.html
http://www.zhongzhu71.com/detail/103.html
http://www.zhongzhu71.com/detail/102.html
http://www.zhongzhu71.com/detail/100.html
http://www.zhongzhu71.com/detail/99.html
http://www.zhongzhu71.com/detail/98.html
http://www.zhongzhu71.com/detail/97.html
http://www.zhongzhu71.com/detail/96.html
http://www.zhongzhu71.com/detail/95.html
http://www.zhongzhu71.com/detail/94.html
http://www.zhongzhu71.com/detail/93.html
http://www.zhongzhu71.com/detail/92.html
http://www.zhongzhu71.com/detail/91.html
http://www.zhongzhu71.com/detail/90.html
http://www.zhongzhu71.com/detail/89.html
http://www.zhongzhu71.com/detail/88.html
http://www.zhongzhu71.com/detail/87.html
http://www.zhongzhu71.com/detail/84.html
http://www.zhongzhu71.com/detail/182.html
http://www.zhongzhu71.com/detail/181.html
http://www.zhongzhu71.com/detail/180.html
http://www.zhongzhu71.com/detail/179.html
http://www.zhongzhu71.com/detail/178.html
http://www.zhongzhu71.com/detail/185.html
http://www.zhongzhu71.com/detail/184.html
http://www.zhongzhu71.com/detail/183.html
http://www.zhongzhu71.com/detail/187.html
http://www.zhongzhu71.com/detail/186.html
http://www.zhongzhu71.com/detail/197.html
http://www.zhongzhu71.com/detail/196.html
http://www.zhongzhu71.com/detail/195.html
http://www.zhongzhu71.com/detail/194.html
http://www.zhongzhu71.com/detail/193.html
http://www.zhongzhu71.com/detail/192.html
http://www.zhongzhu71.com/detail/191.html
http://www.zhongzhu71.com/detail/190.html
http://www.zhongzhu71.com/detail/189.html
http://www.zhongzhu71.com/detail/188.html
http://www.zhongzhu71.com/detail/203.html
http://www.zhongzhu71.com/detail/202.html
http://www.zhongzhu71.com/detail/201.html
http://www.zhongzhu71.com/detail/200.html
http://www.zhongzhu71.com/detail/199.html
http://www.zhongzhu71.com/detail/198.html
http://www.zhongzhu71.com/detail/213.html
http://www.zhongzhu71.com/detail/212.html
http://www.zhongzhu71.com/detail/211.html
http://www.zhongzhu71.com/detail/210.html
http://www.zhongzhu71.com/detail/209.html
http://www.zhongzhu71.com/detail/207.html
http://www.zhongzhu71.com/detail/206.html
http://www.zhongzhu71.com/detail/205.html
http://www.zhongzhu71.com/detail/204.html
http://www.zhongzhu71.com/detail/228.html
http://www.zhongzhu71.com/detail/227.html
http://www.zhongzhu71.com/detail/226.html
http://www.zhongzhu71.com/detail/225.html
http://www.zhongzhu71.com/detail/224.html
http://www.zhongzhu71.com/detail/223.html
http://www.zhongzhu71.com/detail/222.html
http://www.zhongzhu71.com/detail/221.html
http://www.zhongzhu71.com/detail/220.html
http://www.zhongzhu71.com/detail/219.html
http://www.zhongzhu71.com/detail/218.html
http://www.zhongzhu71.com/detail/217.html
http://www.zhongzhu71.com/detail/216.html
http://www.zhongzhu71.com/detail/215.html
http://www.zhongzhu71.com/detail/214.html
http://www.zhongzhu71.com/detail/244.html
http://www.zhongzhu71.com/detail/243.html
http://www.zhongzhu71.com/detail/242.html
http://www.zhongzhu71.com/detail/241.html
http://www.zhongzhu71.com/detail/240.html
http://www.zhongzhu71.com/detail/239.html
http://www.zhongzhu71.com/detail/238.html
http://www.zhongzhu71.com/detail/237.html
http://www.zhongzhu71.com/detail/236.html
http://www.zhongzhu71.com/detail/235.html
http://www.zhongzhu71.com/detail/234.html
http://www.zhongzhu71.com/detail/233.html
http://www.zhongzhu71.com/detail/232.html
http://www.zhongzhu71.com/detail/231.html
http://www.zhongzhu71.com/detail/230.html
http://www.zhongzhu71.com/detail/229.html
http://www.zhongzhu71.com/detail/251.html
http://www.zhongzhu71.com/detail/250.html
http://www.zhongzhu71.com/detail/249.html
http://www.zhongzhu71.com/detail/248.html
http://www.zhongzhu71.com/detail/247.html
http://www.zhongzhu71.com/detail/246.html
http://www.zhongzhu71.com/detail/245.html
http://www.zhongzhu71.com/detail/253.html
http://www.zhongzhu71.com/detail/252.html
http://www.zhongzhu71.com/detail/254.html
http://www.zhongzhu71.com/detail/258.html
http://www.zhongzhu71.com/detail/257.html
http://www.zhongzhu71.com/detail/256.html
http://www.zhongzhu71.com/detail/255.html
http://www.zhongzhu71.com/detail/261.html
http://www.zhongzhu71.com/detail/260.html
http://www.zhongzhu71.com/detail/259.html
http://www.zhongzhu71.com/detail/276.html
http://www.zhongzhu71.com/detail/275.html
http://www.zhongzhu71.com/detail/274.html
http://www.zhongzhu71.com/detail/273.html
http://www.zhongzhu71.com/detail/272.html
http://www.zhongzhu71.com/detail/271.html
http://www.zhongzhu71.com/detail/270.html
http://www.zhongzhu71.com/detail/269.html
http://www.zhongzhu71.com/detail/268.html
http://www.zhongzhu71.com/detail/267.html
http://www.zhongzhu71.com/detail/266.html
http://www.zhongzhu71.com/detail/265.html
http://www.zhongzhu71.com/detail/264.html
http://www.zhongzhu71.com/detail/263.html
http://www.zhongzhu71.com/detail/262.html
http://www.zhongzhu71.com/detail/304.html
http://www.zhongzhu71.com/detail/303.html
http://www.zhongzhu71.com/detail/302.html
http://www.zhongzhu71.com/detail/301.html
http://www.zhongzhu71.com/detail/300.html
http://www.zhongzhu71.com/detail/299.html
http://www.zhongzhu71.com/detail/298.html
http://www.zhongzhu71.com/detail/297.html
http://www.zhongzhu71.com/detail/296.html
http://www.zhongzhu71.com/detail/295.html
http://www.zhongzhu71.com/detail/294.html
http://www.zhongzhu71.com/detail/293.html
http://www.zhongzhu71.com/detail/292.html
http://www.zhongzhu71.com/detail/291.html
http://www.zhongzhu71.com/detail/290.html
http://www.zhongzhu71.com/detail/289.html
http://www.zhongzhu71.com/detail/288.html
http://www.zhongzhu71.com/detail/287.html
http://www.zhongzhu71.com/detail/286.html
http://www.zhongzhu71.com/detail/285.html
http://www.zhongzhu71.com/detail/284.html
http://www.zhongzhu71.com/detail/283.html
http://www.zhongzhu71.com/detail/282.html
http://www.zhongzhu71.com/detail/281.html
http://www.zhongzhu71.com/detail/280.html
http://www.zhongzhu71.com/detail/279.html
http://www.zhongzhu71.com/detail/278.html
http://www.zhongzhu71.com/detail/320.html
http://www.zhongzhu71.com/detail/319.html
http://www.zhongzhu71.com/detail/318.html
http://www.zhongzhu71.com/detail/317.html
http://www.zhongzhu71.com/detail/316.html
http://www.zhongzhu71.com/detail/315.html
http://www.zhongzhu71.com/detail/314.html
http://www.zhongzhu71.com/detail/313.html
http://www.zhongzhu71.com/detail/312.html
http://www.zhongzhu71.com/detail/311.html
http://www.zhongzhu71.com/detail/310.html
http://www.zhongzhu71.com/detail/309.html
http://www.zhongzhu71.com/detail/308.html
http://www.zhongzhu71.com/detail/307.html
http://www.zhongzhu71.com/detail/306.html
http://www.zhongzhu71.com/detail/305.html
http://www.zhongzhu71.com/detail/326.html
http://www.zhongzhu71.com/detail/325.html
http://www.zhongzhu71.com/detail/324.html
http://www.zhongzhu71.com/detail/323.html
http://www.zhongzhu71.com/detail/322.html
http://www.zhongzhu71.com/detail/321.html
http://www.zhongzhu71.com/detail/337.html
http://www.zhongzhu71.com/detail/335.html
http://www.zhongzhu71.com/detail/334.html
http://www.zhongzhu71.com/detail/333.html
http://www.zhongzhu71.com/detail/332.html
http://www.zhongzhu71.com/detail/331.html
http://www.zhongzhu71.com/detail/330.html
http://www.zhongzhu71.com/detail/329.html
http://www.zhongzhu71.com/detail/328.html
http://www.zhongzhu71.com/detail/327.html
http://www.zhongzhu71.com/detail/339.html
http://www.zhongzhu71.com/detail/338.html
http://www.zhongzhu71.com/detail/342.html
http://www.zhongzhu71.com/detail/341.html
http://www.zhongzhu71.com/detail/340.html
http://www.zhongzhu71.com/detail/344.html
http://www.zhongzhu71.com/detail/343.html
http://www.zhongzhu71.com/detail/365.html
http://www.zhongzhu71.com/detail/364.html
http://www.zhongzhu71.com/detail/363.html
http://www.zhongzhu71.com/detail/362.html
http://www.zhongzhu71.com/detail/361.html
http://www.zhongzhu71.com/detail/360.html
http://www.zhongzhu71.com/detail/359.html
http://www.zhongzhu71.com/detail/358.html
http://www.zhongzhu71.com/detail/357.html
http://www.zhongzhu71.com/detail/356.html
http://www.zhongzhu71.com/detail/355.html
http://www.zhongzhu71.com/detail/354.html
http://www.zhongzhu71.com/detail/353.html
http://www.zhongzhu71.com/detail/352.html
http://www.zhongzhu71.com/detail/351.html
http://www.zhongzhu71.com/detail/350.html
http://www.zhongzhu71.com/detail/349.html
http://www.zhongzhu71.com/detail/348.html
http://www.zhongzhu71.com/detail/347.html
http://www.zhongzhu71.com/detail/346.html
http://www.zhongzhu71.com/detail/345.html
http://www.zhongzhu71.com/detail/372.html
http://www.zhongzhu71.com/detail/371.html
http://www.zhongzhu71.com/detail/370.html
http://www.zhongzhu71.com/detail/369.html
http://www.zhongzhu71.com/detail/368.html
http://www.zhongzhu71.com/detail/367.html
http://www.zhongzhu71.com/detail/366.html
http://www.zhongzhu71.com/detail/374.html
http://www.zhongzhu71.com/detail/373.html
http://www.zhongzhu71.com/detail/378.html
http://www.zhongzhu71.com/detail/377.html
http://www.zhongzhu71.com/detail/376.html
http://www.zhongzhu71.com/detail/375.html
http://www.zhongzhu71.com/detail/391.html
http://www.zhongzhu71.com/detail/390.html
http://www.zhongzhu71.com/detail/389.html
http://www.zhongzhu71.com/detail/388.html
http://www.zhongzhu71.com/detail/387.html
http://www.zhongzhu71.com/detail/386.html
http://www.zhongzhu71.com/detail/385.html
http://www.zhongzhu71.com/detail/384.html
http://www.zhongzhu71.com/detail/383.html
http://www.zhongzhu71.com/detail/382.html
http://www.zhongzhu71.com/detail/381.html
http://www.zhongzhu71.com/detail/380.html
http://www.zhongzhu71.com/detail/379.html
http://www.zhongzhu71.com/detail/395.html
http://www.zhongzhu71.com/detail/394.html
http://www.zhongzhu71.com/detail/393.html
http://www.zhongzhu71.com/detail/392.html
http://www.zhongzhu71.com/detail/407.html
http://www.zhongzhu71.com/detail/406.html
http://www.zhongzhu71.com/detail/405.html
http://www.zhongzhu71.com/detail/404.html
http://www.zhongzhu71.com/detail/403.html
http://www.zhongzhu71.com/detail/402.html
http://www.zhongzhu71.com/detail/401.html
http://www.zhongzhu71.com/detail/400.html
http://www.zhongzhu71.com/detail/399.html
http://www.zhongzhu71.com/detail/398.html
http://www.zhongzhu71.com/detail/397.html
http://www.zhongzhu71.com/detail/396.html
http://www.zhongzhu71.com/detail/413.html
http://www.zhongzhu71.com/detail/412.html
http://www.zhongzhu71.com/detail/411.html
http://www.zhongzhu71.com/detail/410.html
http://www.zhongzhu71.com/detail/409.html
http://www.zhongzhu71.com/detail/408.html
http://www.zhongzhu71.com/detail/422.html
http://www.zhongzhu71.com/detail/421.html
http://www.zhongzhu71.com/detail/420.html
http://www.zhongzhu71.com/detail/419.html
http://www.zhongzhu71.com/detail/418.html
http://www.zhongzhu71.com/detail/417.html
http://www.zhongzhu71.com/detail/416.html
http://www.zhongzhu71.com/detail/415.html
http://www.zhongzhu71.com/detail/414.html
http://www.zhongzhu71.com/detail/438.html
http://www.zhongzhu71.com/detail/437.html
http://www.zhongzhu71.com/detail/436.html
http://www.zhongzhu71.com/detail/435.html
http://www.zhongzhu71.com/detail/434.html
http://www.zhongzhu71.com/detail/433.html
http://www.zhongzhu71.com/detail/432.html
http://www.zhongzhu71.com/detail/431.html
http://www.zhongzhu71.com/detail/430.html
http://www.zhongzhu71.com/detail/429.html
http://www.zhongzhu71.com/detail/428.html
http://www.zhongzhu71.com/detail/427.html
http://www.zhongzhu71.com/detail/426.html
http://www.zhongzhu71.com/detail/425.html
http://www.zhongzhu71.com/detail/424.html
http://www.zhongzhu71.com/detail/423.html
http://www.zhongzhu71.com/detail/444.html
http://www.zhongzhu71.com/detail/443.html
http://www.zhongzhu71.com/detail/442.html
http://www.zhongzhu71.com/detail/441.html
http://www.zhongzhu71.com/detail/440.html
http://www.zhongzhu71.com/detail/439.html
http://www.zhongzhu71.com/detail/474.html
http://www.zhongzhu71.com/detail/473.html
http://www.zhongzhu71.com/detail/472.html
http://www.zhongzhu71.com/detail/471.html
http://www.zhongzhu71.com/detail/470.html
http://www.zhongzhu71.com/detail/469.html
http://www.zhongzhu71.com/detail/468.html
http://www.zhongzhu71.com/detail/467.html
http://www.zhongzhu71.com/detail/466.html
http://www.zhongzhu71.com/detail/465.html
http://www.zhongzhu71.com/detail/464.html
http://www.zhongzhu71.com/detail/463.html
http://www.zhongzhu71.com/detail/462.html
http://www.zhongzhu71.com/detail/461.html
http://www.zhongzhu71.com/detail/460.html
http://www.zhongzhu71.com/detail/459.html
http://www.zhongzhu71.com/detail/458.html
http://www.zhongzhu71.com/detail/457.html
http://www.zhongzhu71.com/detail/456.html
http://www.zhongzhu71.com/detail/455.html
http://www.zhongzhu71.com/detail/454.html
http://www.zhongzhu71.com/detail/453.html
http://www.zhongzhu71.com/detail/452.html
http://www.zhongzhu71.com/detail/451.html
http://www.zhongzhu71.com/detail/450.html
http://www.zhongzhu71.com/detail/449.html
http://www.zhongzhu71.com/detail/448.html
http://www.zhongzhu71.com/detail/447.html
http://www.zhongzhu71.com/detail/446.html
http://www.zhongzhu71.com/detail/445.html
http://www.zhongzhu71.com/detail/504.html
http://www.zhongzhu71.com/detail/503.html
http://www.zhongzhu71.com/detail/502.html
http://www.zhongzhu71.com/detail/501.html
http://www.zhongzhu71.com/detail/500.html
http://www.zhongzhu71.com/detail/499.html
http://www.zhongzhu71.com/detail/498.html
http://www.zhongzhu71.com/detail/497.html
http://www.zhongzhu71.com/detail/496.html
http://www.zhongzhu71.com/detail/495.html
http://www.zhongzhu71.com/detail/494.html
http://www.zhongzhu71.com/detail/493.html
http://www.zhongzhu71.com/detail/492.html
http://www.zhongzhu71.com/detail/491.html
http://www.zhongzhu71.com/detail/490.html
http://www.zhongzhu71.com/detail/489.html
http://www.zhongzhu71.com/detail/488.html
http://www.zhongzhu71.com/detail/487.html
http://www.zhongzhu71.com/detail/486.html
http://www.zhongzhu71.com/detail/485.html
http://www.zhongzhu71.com/detail/484.html
http://www.zhongzhu71.com/detail/483.html
http://www.zhongzhu71.com/detail/482.html
http://www.zhongzhu71.com/detail/481.html
http://www.zhongzhu71.com/detail/480.html
http://www.zhongzhu71.com/detail/479.html
http://www.zhongzhu71.com/detail/478.html
http://www.zhongzhu71.com/detail/477.html
http://www.zhongzhu71.com/detail/476.html
http://www.zhongzhu71.com/detail/475.html
http://www.zhongzhu71.com/detail/528.html
http://www.zhongzhu71.com/detail/527.html
http://www.zhongzhu71.com/detail/526.html
http://www.zhongzhu71.com/detail/525.html
http://www.zhongzhu71.com/detail/524.html
http://www.zhongzhu71.com/detail/523.html
http://www.zhongzhu71.com/detail/522.html
http://www.zhongzhu71.com/detail/521.html
http://www.zhongzhu71.com/detail/520.html
http://www.zhongzhu71.com/detail/519.html
http://www.zhongzhu71.com/detail/518.html
http://www.zhongzhu71.com/detail/517.html
http://www.zhongzhu71.com/detail/516.html
http://www.zhongzhu71.com/detail/515.html
http://www.zhongzhu71.com/detail/514.html
http://www.zhongzhu71.com/detail/513.html
http://www.zhongzhu71.com/detail/512.html
http://www.zhongzhu71.com/detail/511.html
http://www.zhongzhu71.com/detail/510.html
http://www.zhongzhu71.com/detail/509.html
http://www.zhongzhu71.com/detail/508.html
http://www.zhongzhu71.com/detail/507.html
http://www.zhongzhu71.com/detail/506.html
http://www.zhongzhu71.com/detail/505.html
"""

for key,value in enumerate(urls.split()):

    if (key + 1) % 10 == 0:
        b = random.randint(5,10)
        time.sleep(b)

    get_baidu_html(value.strip())

print(f"已经收录了{len(result_shou)}")


