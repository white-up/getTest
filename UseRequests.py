import requests
from bs4 import BeautifulSoup

h = 'a.html'

if __name__ == '__main__':
    f = open('a.html','r',encoding='utf-8').read()
    html = BeautifulSoup(f, 'html.parser')
    list = html.find_all('a','wordBreakWord')
    print(len(list))
    for line in list:
        print(line)
        print('--------------------')
