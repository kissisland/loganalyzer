import os
logfile_path = r'E:\会计网日志分析\logfile'
def readLogfile():
    all_file_name_list = []
    for i in os.listdir(logfile_path):
        if i.endswith('.log'):
            all_file_name_list.append(os.path.splitext(i)[0])
    return all_file_name_list

def writeLogfile():
    for i in os.listdir(logfile_path):
        if i.endswith('.log'):
            os.rename(r'{}\{}'.format(logfile_path, i), r'{}\{}已处理'.format(logfile_path, i))



