
import jieba
import networkx

inputFile = 'shanguo.txt'
stopWordFile = 'stopWords.txt'
outputFile = 'name_' + inputFile
StopWordList = []
counts = {}


def loadStopWord():
    file = open(stopWordFile, 'r', encoding='utf-8')
    for line in file:
        StopWordList.append(line.strip('\n'))


def loadInputFile():
    file = open(inputFile, 'r', encoding='utf-8').read()
    words = jieba.lcut(file)
    for word in words:
        if len(word) == 1 or word in StopWordList:
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            key = "孔明"
        elif word == "关公" or word == "云长":
            key = "关羽"
        elif word == "玄德" or word == "玄德曰":
            key = "刘备"
        elif word == "孟德" or word == "丞相":
            key = "曹操"
        else:
            key = word
        counts[key] = counts.get(key, 0) + 1


def creatData():
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print(items)
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

def showRelation():
    g = networkx.MultiGraph()


if __name__ == '__main__':
    loadStopWord()
    loadInputFile()
    creatData()
