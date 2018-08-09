import psutil, time
import subprocess


def judgeprocess(processname):
    pl = psutil.pids()

    try:
        for pid in pl:
            if psutil.Process(pid).name() == processname:
                return True
        else:
            return False

    except Exception:
        print("发生异常，叼")
        return False


while True:
    if judgeprocess('check_paurl.exe'):
        print("程序还在运行中。。。。")
    else:
        print("程序意外关闭了。马上重新打开...")
        subprocess.Popen("E:\project\loganalyzer\dist\check_paurl.exe", shell=True)
        # os.system("E:\project\loganalyzer\dist\check_paurl.exe")

    time.sleep(600)
# for i in hasprocess('check_paurl.exe'):
#     print(os.kill(i, signal.SIGILL))