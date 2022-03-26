# 计算机202 马湘明
dicTXL = {'name': ['张笑霞', '马湘明', '陈慧君'],
          'phone': ['13912345678', '13900001111', '13900002222'],
          'QQ': ['1819122001', '1819122002', '1819122003']
          }
dicAdd = {'name': ['周健', '文宠智', '覃家贵'],
          'phone': ['13912349876', '13911223344', '13988880911'],
          'QQ': ['1819122004', '1819122005', '1819122006']
          }
dicWechat = {'name': ['张笑霞', '马湘明', '陈慧君', '周健', '文宠智', '覃家贵'],
             'Wechat': ['xx007', 'gang1001', 'jack w', 'liu666']
             }
'''
or 
dicTXL = [
    {'name': 'a',
     'phone': '123', 
     'QQ': '123'
    },
    {'name': 'a',
     'phone': '123', 
     'QQ': '123'
    }
    ...
]
'''
import prettytable


def mergeList(dic):
    listName = dicTXL.get('name')
    addName = dic.get('name')
    addPhone = dic.get('phone')
    addQQ = dic.get('QQ')
    for i, name in enumerate(addName):
        if name not in listName:
            dicTXL.get('name').append(name)
            dicTXL.get('phone').append(addPhone[i])
            dicTXL.get('QQ').append(addQQ[i])
        else:
            print('{}信息已存在', name)


def addWechatAndEmail(dic):
    dicTXL['Wechat'] = []
    dicTXL['email'] = []
    for i, name in enumerate(dicTXL.get('name')):
        try:
            index = dic.get('name').index(name)
            if len(dicWechat.get('Wechat')) < index:
                dicTXL['Wechat'].append(dicTXL['phone'][index])
            else:
                dicTXL['Wechat'].append(dicTXL['phone'][index])
        except ValueError:
            dicTXL['Wechat'].append(dicTXL['phone'][i])
        dicTXL['email'].append(dicTXL['QQ'][i] + '@qq.com')


def inputGetIndex():
    flag_name = True
    while flag_name:
        select = input('people name')
        if select in dicTXL.get('name'):
            index = dicTXL.get('name').index(select)
            return index
        else:
            print('name error')


def showUser(index):
    tb = prettytable.PrettyTable()
    tb.field_names = dicTXL.keys()
    if index == -1:
        for i, name in enumerate(dicTXL.get('name')):
            user = []
            for key in dicTXL.keys():
                user.append(dicTXL.get(key)[i])
            tb.add_row(user)
        print(tb)
    else:
        user = []
        for key in dicTXL.keys():
            user.append(dicTXL.get(key)[index])
        tb.add_row(user)
        print(tb)


def updateUser(index):
    flag_item = True
    while flag_item:
        item = input('Please enter modification items')
        if item in ['name', 'QQ', 'email', 'Wechat', 'phone']:
            value = input('input value')
            dicTXL[item][index] = value
            print('yes')
            flag_item = False
        else:
            print('item error')


def menu():
    flag_menu = True
    while flag_menu:
        select = input('which do you want to do\n查询所有 1\n修改个人 2\n查询个人 3\n结束 4\n')
        if int(select) in range(1, 5):
            return int(select)
        else:
            print('error again')


if __name__ == '__main__':
    mergeList(dicAdd)
    addWechatAndEmail(dicWechat)
    flag = True
    while flag:
        select = menu()
        if select == 1:
            showUser(-1)
        if select == 2:
            updateUser(inputGetIndex())
        if select == 3:
            showUser(inputGetIndex())
        if select == 4:
            flag = False
