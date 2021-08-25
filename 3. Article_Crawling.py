### 매일경제 크롤링 ###
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import urllib
import time
from tqdm.notebook import tqdm
import re
import requests

url1 = 'https://find.mk.co.kr/new/search.php?pageNum={num}&cat=&cat1=&media_eco=&pageSize=10&sub=all&dispFlag=OFF&page=news&s_kwd=&s_page=news&go_page=&ord=1&ord1=1&ord2=0&'
url2 = 's_keyword={keyword}&s_i_keyword=&s_author=&y1=1991&m1=01&d1=01&y2=2021&m2=06&d2=03&ord=1&area=ttbd'
html = url1 + url2
reponse = urlopen(html.format(num = 1, keyword=urllib.parse.quote('일론 머스크 코인')))
soup = BeautifulSoup(reponse,'html.parser')
#제목
soup.find_all('span', 'art_tit')[0].a.get_text()
#url
soup.find_all('span', 'art_tit')[0].a.get('href')
# 언론사 + 시간
soup.find_all('div', 'sub_list')[0].find_all('span','art_time')[0].text

mktitle = []
mkurl = []
mktime = []
url1 = 'https://find.mk.co.kr/new/search.php?pageNum={num}'
url2 = '&cat=&cat1=&media_eco=&pageSize=20&sub=news&dispFlag=OFF&page=news&s_kwd=%B8%D3%BD%BA%C5%A9+%C4%DA%C0%CE&s_page=news&go_page=&ord=1&ord1=1&ord2=0&s_keyword=%B8%D3%BD%BA%C5%A9+%C4%DA%C0%CE&s_i_keyword=%B8%D3%BD%BA%C5%A9+%C4%DA%C0%CE&s_author=&y1=1991&m1=01&d1=01&y2=2021&m2=06&d2=03&ord=1&area=ttbd'
html = url1 + url2

for i in range(1, 43, 1):
    reponse = urlopen(html.format(num=i))
    soup = BeautifulSoup(reponse, 'html.parser')

    for j in range(0, 18, 1):
        t = soup.find_all('span', 'art_tit')[j].a.get_text()
        mktitle.append(t)
        u = soup.find_all('span', 'art_tit')[j].a.get('href')
        mkurl.append(u)
        ti = soup.find_all('div', 'sub_list')[j].find_all('span','art_time')[0].text
        mktime.append(ti)
    time.sleep(0.25)

mk = pd.DataFrame({'title': mktitle, 'url' : mkurl, 'time_raw' : mktime})

journal = []
for i in range(0, len(mk['time_raw'])):
    jour = mk['time_raw'][i].split('\xa0')[0]
    jour = jour.replace(' ','')
    journal.append(jour)

time = []
for i in range(0, len(mk['time_raw'])):
    year = mk['time_raw'][i].split('\xa0')[1].split(' ')[0].replace("년", '')
    month = mk['time_raw'][i].split('\xa0')[1].split(' ')[1].replace("월", '')
    day = mk['time_raw'][i].split('\xa0')[1].split(' ')[2].replace("일", '')
    ft = year+'-'+month+'-'+day
    time.append(ft)

mk = pd.DataFrame({'title': mktitle, 'url' : mkurl, 'time_raw' : mktime, 'journal':journal, 'time': time})
mk.to_excel('mk_article.xlsx')

mk['timestamp'] = pd.to_datetime(mk['time'], format = ('%Y-%m-%d'))
mk_copy = pd.DataFrame.copy(mk)
mk_copy = mk_copy.drop(index=range(198,216,1), axis=0)
mk_copy.reset_index(drop=True, inplace=True)
mk_copy['timestamp'] = pd.to_datetime(mk_copy['time'], format = ('%Y-%m-%d'))
mk_copy.to_excel('mk_article_final.xlsx')


#네이버 크롤링
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import time
from tqdm.notebook import tqdm
import re
from datetime import datetime, timedelta

title = []
art_url = []
journal = []
date = []
reponse = urlopen(html)
for i in tqdm(range(1, 4002, 10)):
    html = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%22%EB%A8%B8%EC%8A%A4%ED%81%AC%22%20%EC%BD%94%EC%9D%B8&sort=0&photo=0&field=0&pd=3&ds=2020.07.01&de=2020.07.31&cluster_rank=23&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20200701to20200731,a:all&start={num}'
    reponse = urlopen(html.format(num=i))
    soup = BeautifulSoup(reponse, 'html.parser')

    for n in range(0,len(soup.find_all(class_='news_tit'))):
        t = soup.find_all(class_='news_tit')[n].get('title')
        title.append(t)
        a = soup.find_all(class_='news_tit')[n].get('href')
        art_url.append(a)
        j = soup.find_all(class_='info press')[n].text.split(' ')[0]
        journal.append(j)

    for k in range(0,len(soup.find_all('span', 'info'))):
        d = soup.find_all('span', 'info')[k].text
        p = re.compile('.?.?.?.?.?면')
        m = p.match(d)
        if m:
            continue
        else:
            date.append(d)
    time.sleep(0.25)
df_result = pd.DataFrame({'title' : title, 'url':art_url, 'journal':journal, 'date':date})
df_result.drop_duplicates(keep='first', inplace = True)
df_result.to_excel('naver_2020_07.xlsx')

### 파일 합치기 ###
import pandas as pd
import re
from datetime import datetime, timedelta

art06 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_06.xlsx')
art07= pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_07.xlsx')
art08 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_08.xlsx')
art09 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_09.xlsx')
art010 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_10.xlsx')
art011 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_11.xlsx')
art012 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2020_12.xlsx')
art111 = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2021_01.xlsx')
art112= pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2021_02.xlsx')
art113= pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2021_03.xlsx')
art114= pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2021_04.xlsx')
art115= pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/naver_2021_05.xlsx')

art_concat = pd.concat([art06, art07, art08, art09, art010, art011, art012, art111, art112, art113, art114, art115],ignore_index = True)
art_concat.to_excel('art_concat.xlsx')
#art_concat = pd.read_excel('C:/Users/Anony/PycharmProjects/pythonProject1/art_concat.xlsx')
df_art = pd.DataFrame.copy(art_concat)

df_art['date_re'] = ''
p2 = re.compile('.?일 전')
for i in range(0, len(df_art['date'])):
    a = df_art['date'][i]
    m2 = p2.match(a)
    crawdate = datetime.strptime('2021.06.03.', '%Y.%m.%d.')
    if m2:
        df_art['date_re'][i] = crawdate - timedelta(days=int(df_art['date'][i].split('일')[0]))
    else :
        df_art['date_re'][i] = pd.to_datetime(df_art['date'][i])


df_art['date_re'][0].strftime('%Y-%m-%d')

list_s = []
for i in range(0,len(df_art['date_re'])):
    a = df_art['date_re'][i].strftime('%Y-%m-%d')
    list_s.append(a)
df_art['date_str'] = list_s
df_art.drop(['Unnamed: 0'], axis=1, inplace = True)
df_art.to_excel('naver_art_final.xlsx')
