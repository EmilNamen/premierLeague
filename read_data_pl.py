import csv


def readCSV(home, visitor, season, matrix, index):
    with open(season + '/1-premierleague.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == home:
                if int(row[3].split('-')[0]) > int(row[3].split('-')[1]):
                    matrix[index][2] = matrix[index][2] + 1

            if row[2] == visitor:
                if int(row[3].split('-')[0]) < int(row[3].split('-')[1]):
                    matrix[index][3] = matrix[index][3] + 1

            if row[1] == home:
                # home goals scored before the match
                matrix[index][8] = matrix[index][8] + int(row[3].split('-')[0])

            if row[2] == visitor:
                # away goals scored before the match
                matrix[index][9] = matrix[index][9] + int(row[3].split('-')[1])

            if row[1] == home:
                # home goals scored before the match
                matrix[index][4] = matrix[index][4] + int(row[3].split('-')[1])

            if row[2] == visitor:
                # away goals scored before the match
                matrix[index][5] = matrix[index][5] + int(row[3].split('-')[0])


    return matrix

def readnewCSV2015(home, visitor, matrix, index):
    with open('2010s/2015.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == home:
                if int(row[1].split('-')[0]) > int(row[1].split('-')[1]):
                    matrix[index][2] = matrix[index][2] + 1
                # home goals scored before the match as a home team
                matrix[index][8] = matrix[index][8] + int(row[1].split('-')[0])
                # home goals received before the match as a home team
                matrix[index][4] = matrix[index][4] + int(row[1].split('-')[1])
            if row[2] == visitor:
                if int(row[1].split('-')[0]) < int(row[1].split('-')[1]):
                    matrix[index][3] = matrix[index][3] + 1
                # away goals scored before the match as a visitor team
                matrix[index][9] = matrix[index][9] + int(row[1].split('-')[1])
                # away goals scored before the match as a visitor team
                matrix[index][5] = matrix[index][5] + int(row[1].split('-')[0])

    return matrix
