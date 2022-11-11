import time

class account:
    def __init__(self,name,password,birth, authority):
        self.name = name
        self.password = password
        self.birth = birth
        self.authority = authority

def login():
    """
    处理是否在account的账号
    不在直接退出
    在，返回用户信息
    :return:
    """
    info = ''
    with open("./resource/account.txt",mode='r',encoding='utf') as r:
        info = r.read()
    print(info)
    infoList = info.split('\n')
    for i in infoList:
        if "#" not in i:
            detail = i.split(' ')
            print(detail)
    print(type(infoList[1]))# string
    print(infoList[1])
    return infoList[1]


def logGame(s):
    print("写日志")
    print("------", s)

def logAlert(s):
    print("写日志")
    print("------", s)

def check():
    print("检测")
    print("read banList")
    while True:
        time.sleep(180)
        err = True
        if err:
            break
    logGame("记录游戏运行情况")
    err = True
    if err:
        kill_game()
    pass


def kill_game():
    print("停止")
    alert()


def alert():
    print("告警")
    print("写到警告文本")
    print("记录游戏违规情况")


def big():
    print("fork一个进程")
    logGame("pid,name,start,account")
    check()


def analyse():
    print("分析功能")
    pass


def package():
    print("打包功能")
    pass




def dealAuthority(info):
    if info[3] == '1':
        print("当前登录的用户权限不够，无法执行相应功能")
        exit(1)


if __name__ == '__main__':
    print("欢迎进入游戏管理系统")
    print("1.我想玩游戏！！！")
    print("2.查看玩游戏状态")
    print("3.打包日志文件")
    x = input("请选择功能")
    if x == '1':
        info = login()
        big()
    if x == '2':
        info = login()
        dealAuthority(info)
        analyse()
    if x == '3':
        info = login()
        dealAuthority(info)
        package()
