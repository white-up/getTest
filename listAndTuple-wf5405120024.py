# 计算机202 马湘明
InfoList = ['姓名', '性别', '一百米', '三千米', '跳远', '跳高', '田径', '跨栏', '接力赛跑']
keyMaxLen = []

userInfoList = [
    ['蒋文波', '男', 1, 1, 0, 0, 1, 1, 0],
    ['舒睿', '女', 0, 1, 0, 1, 0, 1, 1],
    ['舒心雨', '女', 0, 0, 1, 0, 1, 0, 1],
    ['袁昊', '男', 0, 1, 1, 1, 0, 0, 0],
    ['张宏', '女', 1, 0, 1, 0, 0, 0, 1],
    ['龚开宸', '男', 0, 0, 0, 0, 1, 1, 1],
    ['马湘明', '男', 1, 1, 1, 1, 1, 1, 1],
    ['陈慧君', '女', 1, 0, 0, 1, 1, 1, 0]
]
chara = '|'

'''
可以使用目标输出
import prettytable
tb = prettytable.PrettyTable()
tb.field_names = InfoList
tb.add_all(userInfoList)
或者
for user in userInfoList:
    tb.add_row(user)
print(tb)
'''
def printRows(list):
    # maxsize
    for i, item in enumerate(InfoList):
        keyMaxLen.append(max(len(item), len(str(InfoList[i]))))
    rows = list.copy()
    rows.insert(0, InfoList)
    for row in rows:
        R = ''
        for i, r in enumerate(row):
            l = keyMaxLen[i] + 4
            vau = r
            if r == 1:
                vau = '是'
            if r == 0:
                vau = ''
            s = str(vau).center(l, chr(12288))
            s = chara + s[1:len(s)]
            R += s
        R += chara
        print(R)


# 超过项
def selectCount(count):
    userSelectCount = []
    for user in userInfoList:
        cou = 0
        for i in range(2, len(user)):
            cou += user[i]
        if cou >= count:
            userSelectCount.append(user)
    return userSelectCount


# 性别
def selectSex(sex):
    userSelectSex = []
    for user in userInfoList:
        if user[1] == sex:
            userSelectSex.append(user)
    return userSelectSex


def selectItem(index):
    userSelectItem = []
    for user in userInfoList:
        if user[index]:
            userSelectItem.append(user)
    return userSelectItem


def getCount(user):
    count = 0
    for i in range(2, len(user)):

        count += user[i]
    return count


def selectMax(sex):
    user = None
    count = -1
    for u in userInfoList:
        if u[1] == sex:
            if getCount(u) > count:
                user = u
    return user


if __name__ == '__main__':
    print('all')
    printRows(userInfoList)
    print('项目大于2')
    printRows(selectCount(2))
    print('女性选手')
    printRows(selectSex('女'))
    print('3000m参与')
    printRows(selectItem(3))
    print('参赛最多男/女')
    man = selectMax('男')
    woman = selectMax('女')
    users = [man, woman]
    printRows(users)
