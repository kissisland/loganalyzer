import time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

urls = """
http://www.sohu.com/a/239594021_100160649
http://www.sohu.com/a/239592610_100160649
http://www.sohu.com/a/239428999_100160649
http://www.sohu.com/a/238809770_100160649
http://www.sohu.com/a/238430651_100160649
http://www.sohu.com/a/238237575_100160649
"""

index = 0
def flush_read(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'E:\chromedriver.exe')

    for _ in range(273):
        try:
            driver.get(url)
            time.sleep(random.randint(1,2))
            read = driver.find_element_by_xpath("//span[@class='read-num']").text
            print(read)
        except Exception as e:
            print("发生了一个异常。")
    driver.close()

for i in urls.split():
    flush_read(i.strip())

