import zipfile
import time
def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd= bytes(password, "utf8" ))
        print("压缩包密码是" + password)  #破解成功
    except:
        pass  #失败，就跳过

def main():
    zipFile = zipfile.ZipFile('gualan.zip')   
    PwdLists = open('passdict.txt')   #读入所有密码
    for line in PwdLists.readlines():   #挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
    main()
time.sleep(500)