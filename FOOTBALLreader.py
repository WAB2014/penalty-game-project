import csv

teamname = 'Tottenham'
goals = 0
wins = 0
losses = 0
draws = 0
with open('footieINFO.csv', 'r') as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        if row[2] == teamname:    #games played by team at home
            goals = goals + int(row[4]) #goals
            print(', '.join(row[1:7]))   
            if int(row[4]) > int(row[5]): #home goals greater than away goals
                wins = wins + 1      #wins
            elif int (row[4]) < int(row[5]):#away goals greater than away goals
                losses = losses +1  #losses
            else:
                draws = draws +1  #draws
                
        if row[3] == teamname:    #games played by team away
            goals = goals + int(row[5]) #goals
            print(', '.join(row[1:7]))
            if int(row[5]) > int(row[4]): #home goals greater than away goals
                wins = wins + 1      #wins
            elif int (row[5]) < int(row[4]):#away goals greater than away goals
                losses = losses +1  #losses
            else:
                draws = draws +1  #draws
        #if i == 5:
        #    break
        i += 1

print('Goals by '+teamname+': '+str(goals))
print('Wins: '+str(wins))
print('Losses: '+str(losses))
print('Draws: '+str(draws))
print(teamname+','+str(goals)+','+str(wins)+','+str(losses)+','+str(draws))
statsfile = open('/Users/William03/GitHub/penalty-game-project/statsfile.csv','a')
statsfile.write('\n'+teamname+','+str(goals)+','+str(wins)+','+str(losses)+','+str(draws))
statsfile.close()
