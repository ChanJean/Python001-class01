import requests
import lxml.etree
import pandas as pd

url = 'https://movie.douban.com/subject/1292052/'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

header = {}
header['user-Agent'] = user_agent
response = requests.get(url, headers=header)

selector = lxml.etree.HTML(response.text)

counter = 0
movieList = []
movieList.append('=== Top 10 Movies List ===')
print('Run Start')

movie_title = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'title:{movie_title}')
movie_time = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'time:{movie_time}')
mylist =[movie_title, movie_time]  

movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('./movieList2.csv', encoding='utf8',
              index=False, header=False)

print('mylist')