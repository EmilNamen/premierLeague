import urllib2
from bs4 import BeautifulSoup


def getTopScorers(home, visitor, matrix, index):
    topScorers = []
    response = urllib2.urlopen('https://www.premierleague.com/stats')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for div in soup.findAll("div", {"data-stat-header": "DashboardPlayerStats"}):
        if(div.findAll('div', {"data-body": 'Official Premier League Stats - Goals'})):
            for li1 in div.findAll("li", {"class": "statsHero"}):
                playeri = u''.join(
                    ('https://www.premierleague.com', li1.a['href'])).encode('utf-8')
                responsei = urllib2.urlopen(playeri)
                soupi = BeautifulSoup(responsei.read(), 'html.parser')
                topScorers.append(soupi.findAll("div", {"class": "info"})[
                                  0].text.encode('utf-8').strip())
                #print (li1.a.text + ' ' + soupi.findAll("div",{"class": "info"})[0].text.strip())

            for li2 in div.findAll("li", {"class": "statsRow"}):
                playerj = u''.join(
                    ('https://www.premierleague.com', li2.a['href'])).encode('utf-8')
                responsej = urllib2.urlopen(playerj)
                soupj = BeautifulSoup(responsej.read(), 'html.parser')
                topScorers.append(soupj.findAll("div", {"class": "info"})[
                                  0].text.encode('utf-8').strip())
                #print (li2.a.text + ' ' + soupj.findAll("div",{"class": "info"})[0].text.strip())

    #print topScorers

    for scorer in topScorers:
        if scorer == home:
            matrix[index][0] = 1
        if scorer == visitor:
            matrix[index][1] = 1

    return matrix
