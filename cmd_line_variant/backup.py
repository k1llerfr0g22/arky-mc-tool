import os
import datetime

#datetime_object = datetime.datetime.now()
#date_object = datetime.date.today()

with open('backup_count.txt', 'r') as file:
    data = file.read().replace('\n', '')


backup_name = "backup" + data #+ " " + str(date_object)
os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos/backups && mkdir " + str(backup_name))
os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos/ && cp world -r ~/code/server/minecraft/aternos/backups/" + backup_name)
