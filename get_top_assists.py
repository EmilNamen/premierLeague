import urllib2
from bs4 import BeautifulSoup


def getTopAssists(home, visitor, matrix, index):
    topAssists = []
    response = urllib2.urlopen('https://www.premierleague.com/stats')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll("div", {"data-stat-header": "DashboardPlayerStats"}):
        if(div.findAll('div', {"data-body": 'Official Premier League Stats - Assists'})):
            for li1 in div.findAll("li", {"class": "statsHero"}):
                playeri = u''.join(
                ('https://www.premierleague.com', li1.a['href'])).encode('utf-8')
                responsei = urllib2.urlopen(playeri)
                soupi = BeautifulSoup(responsei.read(), 'html.parser')
                topAssists.append(soupi.findAll("div", {"class": "info"})[0].text.encode('utf-8').strip())

            for li2 in div.findAll("li", {"class": "statsRow"}):
                playerj = u''.join(
                ('https://www.premierleague.com', li2.a['href'])).encode('utf-8')
                responsej = urllib2.urlopen(playerj)
                soupj = BeautifulSoup(responsej.read(), 'html.parser')
                playerNamej = li2.a.text.encode('utf-8')
                topAssists.append(soupj.findAll("div", {"class": "info"})[0].text.encode('utf-8').strip())

    #print topAssists

    for assist in topAssists:
        if assist == home:
            matrix[index][6] = 1
        if assist == visitor:
            matrix[index][7] = 1

    return matrix
