
class Punto():
    def __init__(self, x, y):
        self.x, self.y = x, y

class Rect():
    def __init__(self, name, h, w):
        self.name = name
        self.width  = w
        self.height = h
        self.rotation = False
    
    def rotar(self):
        self.width, self.height = self.height, self.width
        self.rotation = not self.rotation

    def getPosicionX(self):
        return self.x + self.width

    def getPosicionY(self):
        return self.y + self.height
    
    def getArea(self):
        return self.width*self.height


    def imprimir(self, pos=False):
        if (pos):
            self (self.name, self.x, self.y)
        else:
            print(self.name, self.width, self.height, self.rotation)
def getData(filename, d,c):
    #get data from the file 
    lines = [line.rstrip('\n') for line in open(filename, "r") ]

    #get dimensiones
    d.append(int(lines[0].split(" ")[0]))
    d.append(int(lines[0].split(" ")[1]))
    
    #save the cortes dimensions and clean the data for empty spaces
    for i in range(2, len(lines)):
        c.append(lines[i].split(" "))
        #c[i-2].pop() if (i != len(lines)-1) else -1      
    #print (d, c)
    #returns number of plachas cause numbers are hard to deal with as refernces
    return int(lines[1])

def disposicion():

def ordenar(n, stop, c, cts, data):
    mejorSec, newConf, l = [c], [], 0
    disposicion("""n, 10, 0.2, 0.5, mejorSec, newConf, l""")


def main():
    import timeit
    start = timeit.default_timer()
    dim, cortes = [], []
    num = getData("test", dim, cortes)
    
    cuts = []
    for c in cortes:
        for i in range (0, int(c[3])): 
           cuts.append(Rect(c[0], int(c[1]), int(c[2])))
    #empty list of xs and ys
    xs, ys = [[]] * num, [[]] * num
    #hago trampa

    def comparator( rectangle ) :
        return rectangle.getArea()
    cuts.sort(key = comparator, reverse=True)
   

    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == "__main__":
    main()