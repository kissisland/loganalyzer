import time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def flush_read(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'E:\chromedriver.exe')

    try:
        driver.get(url)
        time.sleep(random.randint(1,2))
        read = driver.find_element_by_xpath("//span[@class='read-num']").text
        print(read)
    except Exception as e:
        print("发生了一个异常。")
    driver.close()

flush_read("http://xawjw.xa.gov.cn/ptl/def/def/index_937_7753.html")
