from urllib.request import urlopen

from bs4 import BeautifulSoup

defaultURL = 'https://coindar.org'

events = []
x = []
rows = 0

html = urlopen(defaultURL + "/en/events/2018/1")

bsObj = BeautifulSoup(html, "html.parser")

links = bsObj.findAll('div', attrs={'class':'event'})

for link in links:
    for a in link.findAll('a', href=True):
        #print(a.get_text(strip=True))
        if a.get_text(strip=True):
            #link_text.append(a['href'])
            if a['href'].find('event') > 0:
                html_detail = urlopen(defaultURL + a['href'])
                bsObj_detail = BeautifulSoup(html_detail, "html.parser")
                #print(bsObj_detail.find('title').get_text(strip=True).split(':')[0].rsplit(' ', 1)[1] + " (" + bsObj_detail.find('title').get_text(strip=True).split(':')[0].rsplit(' ', 1)[0] + ")")
                coin = bsObj_detail.find('title').get_text(strip=True).split(':')[0].rsplit(' ', 1)[1] + " (" + bsObj_detail.find('title').get_text(strip=True).split(':')[0].rsplit(' ', 1)[0] + ")"
                title = bsObj_detail.find('span', attrs={'class': 'title'}).get_text(strip=True).split(':')[1]
                type = bsObj_detail.find('div', attrs={'class':'type'}).get_text(strip=True)
                date = bsObj_detail.find('span', attrs={'class':'start'}).get_text(strip=True)[0:10]
                proof = bsObj_detail.find('div', attrs={'class':'source'}).find('a', href=True)['href']
                events.append([coin, title, type, date, proof])


file = open("coindar_crawl_result.txt", "w", encoding='utf-8')

file.write('<table width="100%" border="1px solid black" border-collapse="collapse"><tr><td>코인</td><td>내용</td><td>종류</td><td>날짜</td><td>증명 링크</td></tr>')

for a in events:
    file.write('<tr>\n')
    file.write('<td>' + a[0] + '</td>\n')
    file.write('<td>' + a[1] + '</td>\n')
    file.write('<td>' + a[2] + '</td>\n')
    file.write('<td>' + a[3] + '</td>\n')
    file.write('<td><a href=\"' + a[4] + '\">LINK!!!</a></td>\n')
    file.write('</tr>\n')

file.write('</table>\n')

file.close()