from get_top_scorers import getTopScorers
from get_top_assists import getTopAssists
from get_top_saves import getTopSaves
from read_data_pl import readCSV
from getOutputs import getOutputs

homeTeams = ['Tottenham']
visitorTeams = ['Arsenal']
matrix = [0,0,0,0,0,0,0,0,0]
seasons = ['2000s/2002-03','2000s/2003-04','2000s/2004-05','2000s/2005-06','2000s/2006-07','2000s/2007-08','2000s/2008-09','2000s/2009-10','2010s/2010-11','2010s/2011-12','2010s/2013-14']
outputs = [0,0,0]

for index, season in enumerate(seasons):
    getTopScorers('Tottenham Hotspur','Arsenal',matrix)
    getTopAssists('Tottenham Hotspur','Arsenal',matrix)
    getTopSaves('Tottenham Hotspur','Arsenal',matrix)
    print readCSV('Tottenham','Arsenal',matrix,season)
    print getOutputs('Tottenham','Arsenal',outputs,season)
    matrix = [0,0,0,0,0,0,0,0,0]
    outputs = [0,0,0]
