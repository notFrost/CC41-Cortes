import random
import math
from random import seed

random.seed()

names =['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
nameslen = len(names)
def createPlancha(m): 
    m.append(random.randint(200,5000))
    m.append(random.randint(200,5000))
    m.append(random.randint(1,10))

    return

def createCortes(c, m):
    n = random.randint(1, m[2])*4

    for i in range(0,n):
        c.append([names[i if i<23 else i%nameslen]* (1 if i<nameslen else 2)])
        if (m[2]*2 > n):
            c[i].append(random.randint(0, m[0]))
            c[i].append(random.randint(0,m[1]))
        else:
            c[i].append(random.randint(0, m[0]/2))
            c[i].append(random.randint(0,m[1]/2))
        c[i].append(random.randint(1,1 if n/10<1 else n/10))
    print (c)
    print (m,n)

def write(cortes,m, f):
    s = str(m[0]) + " " + str(m[1]) + "\n" + str(m[2])
    f.write(s)
    for c in cortes:
        s = "\n" + str(c[0]) + " " + str(c[1]) + " " + str(c[2])+" " + str(c[3])
        f.write(s)

fo = open("test.txt", "w")
mesures = []
cortes = []
createPlancha(mesures)
createCortes(cortes, mesures)
write(cortes, mesures, fo)
fo.close()
