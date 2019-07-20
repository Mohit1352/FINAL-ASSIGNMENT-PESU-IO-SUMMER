import csv
import os
import random
files=os.listdir(".\Scraps")
for file in files:
    f=open(".\Scraps\{f}".format(f=file))
    dl=csv.reader(f)
    d=[]
    for row in dl:
        d.append(row)
    f.close()
    random.shuffle(d)
    with open('.\Split\{f}_train.csv'.format(f=file[:-4]), mode='w', newline='') as fil1, open('.\Split\{f}_test.csv'.format(f=file[:-4]), mode='w', newline='') as fil2:
        trainw = csv.writer(fil1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        testw = csv.writer(fil2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        l=len(d)
        train=(int)(0.8*l)
        for i in range(train):
            trainw.writerow(d[i])
        for i in range(train+1,l):
            testw.writerow(d[i])

for file in os.listdir(".\Split"):
    f=open(".\Split\{f}".format(f=file))
    dl=csv.reader(f)
    d1=[]
    d=[]
    r=[]
    c=[]
    t=[]
    for row in dl:
        d1.append(row)
    f.close()
    for i in range(len(d1)):
        r.append(d1[i][4])
        d.append(d1[i][0])
        c.append(d1[i][-6])
        t.append((float(d1[i][-4])+float(d1[i][-5]))/2)
    with open('.\Modified\Mod_{f}'.format(f=file),mode='w',newline='') as fil:
        writer = csv.writer(fil, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(r)):
            writer.writerow([d[i],r[i],c[i],t[i]])
