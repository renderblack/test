import time
answer1='好的，我知道了，您需要兑换'
answer2='金加隆'
answer3='那么，您需要付给我'
answer4='人民币'
question1=input('您好，欢迎来到古灵阁，请问您需要帮助吗？（需要或不需要）')
if question1=='需要':
    question2=input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    if question2=='1':
        print('推荐你去存取款窗口')
    elif question2=='2':
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        question3=input('请问您需要兑换多少金加隆呢？')
        print(answer1+question3+answer2)
        print(answer3+str(int(question3)*51.3)+answer4)
    else:
        print('推荐你去咨询窗口')
        time.sleep(5)
else:
    print('好的，再见。')
time.sleep(5)
ok
