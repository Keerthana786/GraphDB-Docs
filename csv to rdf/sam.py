
import csv
aList=[]
with open("orders.csv", 'r') as f:
    reader = csv.reader(f, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        aList.append(row)

f.close()
for row in aList:
    print(row,"\n")
with open("orders.csv","w") as f:
    writer=csv.writer(f,delimiter=',')
    for row in aList:
        writer.writerow(row)
