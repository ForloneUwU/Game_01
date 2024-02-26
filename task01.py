import csv
# открыть
with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file,delimiter='$'))[1:]
#новый файл
with open('game.csv','w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow('game','name_npc','errorcode','date')

for game, name_npc, errorcode, date in reader:
    if '55' in errorcode:
        replace (date,'00-00-0000')
