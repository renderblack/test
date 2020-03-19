import time
question=input('您好，请输入您的实际工资')
wage=int(question)
if wage<=500:
    print('欢迎进入史塔克穷人帮前三名')
    if 100<wage<=500:
        print('请找弗瑞队长加薪')
    else:
        print('恭喜您荣获“美元队长”称号！')
elif 500<wage<=1000:
    print('祝贺您至少可以温饱了。')
else:
    print('经济危机都难不倒您！')
    if 1000<wage<=20000:
        print('您快比钢铁侠有钱了！')
    else:
        print('您是不是来自于瓦坎达国？')
print('程序结束，5秒后将关闭窗口')
time.sleep(5)