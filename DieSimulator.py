import random
import csv
from collections import Counter
import datetime

dieSides = int(input("How many sides to this die?\n"))
rolls = int(input("How many rolls should be simulated?\n"))
results = []
for i in range(rolls):
    roll = random.randint(1, dieSides)
    
    results.append(roll)

print("\n")
print("Results generated. Writing to file.\n")
dict = Counter(results)


with open('DieSimulatorResult'+str(datetime.datetime.now().timestamp())+'.csv', 'w', newline='') as csvfile:
    fieldnames = ['Number','AmountRolled']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for key, value in dict.items():
       writer.writerow([key, value])
print('Done!')