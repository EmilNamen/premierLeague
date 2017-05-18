import csv

def getOutputs(home, visitor, outputs, season):
  homeGoals = 0
  awayGoals = 0
  with open(season + '/1-premierleague.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      if(row[1] == home and row[2] == visitor):
          if(int(row[3].split('-')[0]) - int(row[3].split('-')[1]) > 0):
              outputs = [1,0,0]
          elif(int(row[3].split('-')[0]) - int(row[3].split('-')[1]) < 0):
              outputs = [0,0,1]
          else:
              outputs = [0,1,0]
    return outputs
