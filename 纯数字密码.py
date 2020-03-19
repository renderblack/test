
import zipfile
import time
import threading
startTime = time.time()
flag = True

def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime-startTime))
        global flag
        flag = False
    except Exception as e:
        print(e)
 
 
def do_main():
    zfile = zipfile.ZipFile("需要破解文件名.zip", 'r')
    for number in range(1, 999999):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()
 
if __name__ == '__main__':
    do_main()
