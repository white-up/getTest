# 计算机202 马湘明 6109120158
import random

import pymysql as pymysql

dictionaries = ['python', 'java', 'hello', 'world']
selectWords = ['Y', 'y', 'N', 'n']


# 内置字典
def getWords():
    words = getWordsByDatabase()
    return words[random.randint(0, len(words) - 1)]
    # return dictionaries[random.randint(0, len(dictionaries) - 1)]


# 连接数据库
def getWordsByDatabase():
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='m08141614',
        db='test2',
        charset='utf8'
    )
    cursor = db.cursor()
    sql = "select * from words;"
    cursor.execute(sql)
    words = []
    for row in cursor.fetchall():
        words.append(row[0])
    return words


def upsetWords(words):
    # 使用内置函数
    """
    listStr = list(words)
    random.shuffle(listStr)
    return ''.join(listStr)
    """
    str = ''

    while words:
        position = random.randrange(len(words))
        str += words[position]
        words = words[:position] + words[(position + 1):]
    return str


if __name__ == '__main__':
    select = 'Y'
    print('        欢迎参加猜单词游戏\n    请把下列各字母组合成一个正确的单词\n')
    while select.upper() == 'Y':
        words = getWords()
        print('乱序后的单词: ' + upsetWords(words))
        guess = input('请你猜: ')
        while guess != words:
            guess = input('继续猜: ')
        print('good')
        select = input('继续猜否(Y/N): ')
        while select not in selectWords:
            select = input('输入正确格式(Y/N): ')
    print('bye')
