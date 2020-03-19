#生成从000000到99999的密码表
f = open('passdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()