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
                coin = bsObj_detail.find('span', attrs={'class': 'title'}).get_text(strip=True).split(':')[0]
                title = bsObj_detail.find('span', attrs={'class': 'title'}).get_text(strip=True).split(':')[1]
                date = bsObj_detail.find('span', attrs={'class':'start'}).get_text(strip=True)[0:10]
                proof = bsObj_detail.find('div', attrs={'class':'source'}).find('a', href=True)['href']
                events.append([coin, title, date, proof])


file = open("coindar_crawl_result.txt", "w", encoding='utf-8')

file.write('<style>\n')
file.write('table {\n')
file.write('    width:100%;\n')
file.write('}\n')
file.write('table, th, td {\n')
file.write('    border: 1px solid black;\n')
file.write('    border-collapse: collapse;\n')
file.write('}\n')
file.write('th, td {\n')
file.write('    padding: 5px;\n')
file.write('    text-align: left;\n')
file.write('}\n')
file.write('table#t01 tr:nth-child(even) {\n')
file.write('    background-color: #eee;\n')
file.write('}\n')
file.write('table#t01 tr:nth-child(odd) {\n')
file.write('   background-color:#fff;\n')
file.write('}\n')
file.write('table#t01 th {\n')
file.write('    background-color: black;\n')
file.write('    color: white;\n')
file.write('}\n')
file.write('</style>\n')

file.write('<table><tr><td>COIN</td><td>TITLE</td><td>DATE</td><td>LINK</td></tr>')

for a in events:
    file.write('<tr>\n')
    file.write('<td>' + a[0] + '</td>\n')
    file.write('<td>' + a[1] + '</td>\n')
    file.write('<td>' + a[2] + '</td>\n')
    file.write('<td><a href=\"' + a[3] + '\">LINK!!!</a></td>\n')
    file.write('<tr>\n')

file.write('</table>\n')

file.close()