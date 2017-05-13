import urllib2
from bs4 import BeautifulSoup


def getTopSaves(home, visitor, matrix):
  topSaves = []
  response = urllib2.urlopen('https://www.premierleague.com/stats')
  html = response.read()
  soup = BeautifulSoup(html, 'html.parser')

  for div in soup.findAll("div", {"data-stat-header": "DashboardPlayerStats"}):
    if(div.findAll('div', {"data-body": 'Official Premier League Stats - Saves'})):
      for li1 in div.findAll("li", {"class": "statsHero"}):
        playeri = u''.join(
            ('https://www.premierleague.com', li1.a['href'])).encode('utf-8')
        responsei = urllib2.urlopen(playeri)
        soupi = BeautifulSoup(responsei.read(), 'html.parser')
        topSaves.append(soupi.findAll("td", {"class": "team"})[
                        0].a.span.text.encode('utf-8').strip())
        #print (li1.a.text + ' ' + soupi.findAll("td", {"class": "team"})[0].a.span.text.strip())

      for li2 in div.findAll("li", {"class": "statsRow"}):
        playerj = u''.join(
            ('https://www.premierleague.com', li2.a['href'])).encode('utf-8')
        responsej = urllib2.urlopen(playerj)
        soupj = BeautifulSoup(responsej.read(), 'html.parser')
        playerNamej = li2.a.text.encode('utf-8')
        topSaves.append(soupj.findAll("td", {"class": "team"})[
                        0].a.span.text.encode('utf-8').strip())
        #print (li2.a.text + ' ' + soupj.findAll("td",{"class": "team"})[0].a.span.text.strip())

  #print topSaves

  for save in topSaves:
    if save == home:
      matrix[4] = 1
    if save == visitor:
      matrix[5] = 1

  return matrix
