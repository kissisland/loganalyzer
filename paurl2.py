def check_and_email(link, f = True):
    try:
        res = requests.get(link)
        if res.status_code != 200:
            sendemail.content = "{}发现以下问题：{}".format(res.url, res.text)
            sendemail.title = "paurl.com访问异常了"
            sendemail.sendEmail()
            print("paurl.com访问异常了")
        elif now_time.hour in [9, 18, 14, 22, 23, 10, 12] and res.status_code == 200 and f:
            sendemail.content = "paurl.com目前运行正常：{}".format(html.fromstring(res.content).xpath("//title/text()")[0])
            sendemail.title = "paurl.com目前运行正常"
            sendemail.sendEmail()
            print("paurl.com目前运行正常：{}".format(html.fromstring(res.content).xpath("//title/text()")[0]))
            return False
        # elif now_time.minute == 0:
        #     return True
        else:
            print("paurl.com目前运行正常：{}".format(html.fromstring(res.content).xpath("//title/text()")[0]))
            return True
    except Exception as e:
        print("check_and_email发生异常：{}".format(e))
        time.sleep(10)
        return check_and_email(link)
if __name__ == '__main__':
    sched_Timer = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, 0, 2) + \
                  timedelta(hours=1)
    link = "http://www.paurl.com"
    flag = True
    while True:
        now_time = datetime.now()
        if now_time > sched_Timer:
            if flag:
                flag = check_and_email(link)
            else:
                check_and_email(link, False)

            sched_Timer += timedelta(minutes=15)

            if now_time.minute == 0: flag = True

            time.sleep((sched_Timer - now_time).seconds)
        else:
            time.sleep((sched_Timer - now_time).seconds)