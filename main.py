from get_top_scorers import getTopScorers
from get_top_assists import getTopAssists
from get_top_saves import getTopSaves
from read_data_pl import readCSV
from read_data_pl import readnewCSV2015
from getOutputs import getOutputs


homeNamePremierLeagueWebPage = ['Tottenham Hotspur','Arsenal','Chelsea','Manchester United','Liverpool','Manchester City','Everton','Southhampton']
homeNameCSV = ['Tottenham','Arsenal','Chelsea','Man United','Liverpool','Man City','Everton','Southhampton']
visitorNamePremierLeagueWebPage = ['Arsenal','Tottenham Hotspur','Manchester United','Chelsea','Manchester City','Liverpool','Southhampton','Everton']
visitorNameCSV = ['Arsenal','Tottenham','Man United','Chelsea','Man City','Liverpool','Southhampton','Everton']
matrix = [[0 for i in range(12)] for j in range(12)]
seasons = ['2000s/2002-03','2000s/2003-04','2000s/2004-05','2000s/2005-06','2000s/2006-07','2000s/2007-08','2000s/2008-09','2000s/2009-10','2010s/2010-11','2010s/2011-12','2010s/2012-13', '2010s/2013-14']
outputs = [0,0,0]
inputs = []


for i,team in enumerate(homeNamePremierLeagueWebPage):
    #print getTopScorers(team, visitorNamePremierLeagueWebPage[i], matrix, i) #matrix[0] & matrix[1]
    #print getTopAssists(team, visitorNamePremierLeagueWebPage[i], matrix,  i) #matrix[2] & matrix[3]
    #print getTopSaves(team, visitorNamePremierLeagueWebPage[i], matrix, i)   #matrix[4] & matrix[5]
    #for season in seasons:
        #print readCSV(homeNameCSV[i],visitorNameCSV[i],season,matrix,i)
    print readnewCSV2015(homeNameCSV[i],visitorNameCSV[i],matrix,i)
