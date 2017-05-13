import csv

def readCSV(home, visitor, matrix, season):
  homeGoals = 0
  awayGoals = 0
  with open(season + '/1-premierleague.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      if(row[1] == home and row[2] == visitor):
        matrix[6] = int(row[3].split('-')[0]) - int(row[3].split('-')[1]) #difference goals home-visitor last game
        break
      if row[1] == home:
        matrix[7] = matrix[7] + int(row[3].split('-')[0]) # home goals scored before the match
      if row[2] == visitor:
        matrix[8] = matrix[8] + int(row[3].split('-')[1]) # away goals scored before the match
    return matrix
