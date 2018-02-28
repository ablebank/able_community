from urllib.request import urlopen
from bs4 import BeautifulSoup

defaultURL = 'https://coindar.org'

events = []
x = []
rows = 0

html = urlopen(defaultURL + "/en/events/2018/2")

bsObj = BeautifulSoup(html, "html.parser")

links = bsObj.findAll('div', attrs={'class':'event'})

def event_type(argument):
    #print(argument)
    if argument == "Release":
        return "출시"
    elif argument == "Announcement":
        return "발표"
    elif argument == "Branding":
        return "브랜딩"
    elif argument == "Update":
        return "업데이트"
    elif argument == "Airdrop":
        return "에어드랍"
    elif argument == "Exchange":
        return "상장"
    elif argument == "Hard fork":
        return "하드포크"
    elif argument == "AMA":
        return "질의응답"
    elif argument == "Swap":
        return "코인교환"
    elif argument == "ICO":
        return "ICO"
    elif argument == "Conference":
        return "컨퍼런스"
    elif argument == "Test":
        return "테스트"
    elif argument == "Law":
        return "규제"
    elif argument == "Burn":
        return "소각"
    elif argument == "Partnership":
        return "파트너쉽"
    elif argument == "Meetup":
        return "밋업"
    else: # default, could also just omit condition or 'if True'
        return "" # No need to break here, it'll stop anyway


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
                type = event_type(bsObj_detail.find('div', attrs={'class':'type'}).get_text(strip=True))
                date = bsObj_detail.find('span', attrs={'class':'start'}).get_text(strip=True)[0:10]
                proof = bsObj_detail.find('div', attrs={'class':'source'}).find('a', href=True)['href']

                events.append([coin, title, type, date, proof])


file = open("coindar_crawl_result.txt", "w", encoding='utf-8')

file.write('<table width="100%" border="1px solid black" border-collapse="collapse"><tr><td><b><span style="font-size: 11pt;">코인</span></b></td><td><b><span style="font-size: 11pt;">일정 내용</span></b></td><td><b><span style="font-size: 11pt;">일정 종류</span></b></td><td><b><span style="font-size: 11pt;">일정 날짜</span></b></td><td><b><span style="font-size: 11pt;">증명 링크</span></b></td></tr>')

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
