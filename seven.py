import jieba
import pymysql

inputFile = 'j.txt'
outputFile = 'JaneEyre_topN.txt'
counts = {}
stopWordFile = 'stopWords.txt'
StopWordList = ['\n', '\r', ' ', ' ']
db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='m08141614',
    db='test2',
    charset='utf8'
)


def loadStopWord():
    file = open(stopWordFile, 'r', encoding='utf-8')
    for line in file:
        StopWordList.append(line.strip('\n'))


def loadInputFile():
    file = open(inputFile, 'r', encoding='utf-8').read()
    words = jieba.lcut(file)
    for word in words:
        if word in StopWordList:
            continue
        counts[word] = counts.get(word, 0) + 1


def saveData():
    # 文件
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    fo = open(outputFile, "a", encoding='utf-8')
    for i in range(20):
        word, count = items[i]
        word = str(word)
        count = str(count)
        fo.write(word)
        fo.write(':')
        fo.write(count)
        fo.write('\n')
    fo.close()
    # 数据库
    if creatTable():
        cursor = db.cursor()
        for i in range(20):
            word, count = items[i]
            word = str(word)
            insert_sql = '''INSERT INTO words(id,word,c) VALUES (%s,%s,%s)'''
            try:
                cursor.execute(insert_sql, args=[i+1, word, count])
                db.commit()
                print('success')
            except Exception:
                print('error(insert)')
        cursor.close()


def creatTable():
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS words')
    creat_table_sql = '''
        create table words(
        id int not null,
        word char(10),
        c int)
    '''
    try:
        cursor.execute(creat_table_sql)
        print('创建表成功')
        return True
    except Exception:
        print('error(creat table)')
        return False
    finally:
        cursor.close()


if __name__ == '__main__':
    loadStopWord()
    loadInputFile()
    saveData()
