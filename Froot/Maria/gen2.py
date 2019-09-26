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


def verificar(xs, ys, corte, pnt):
    bx, sx, by, sy  = 0,0,0,0
    pntx, pnty = 0, 0
    for i in range(0, len (xs)-1):
        if (xs[i]+corte.width == xs[i+1]):
            pntx = 1
            for j in range(0, len (ys)-1): 
                if(pntx == 1 and ys[j]+corte.height == ys[j+1]):
                    bx, by = xs[i], ys[j]
                    pnty = 1
                    break
                elif (ys[j]+corte.height == ys[j+1]):
                    by = ys[j] 
                    pnty = 1
            if (pntx == 1 and pnty == 1):
                sx, sy = bx, by
                break
            elif (pntx == 1 and not sx):
                sx = bx
            elif (pnty == 1 and not sy):
                sy = by
    if (not sx and not sx or 
            sx and not sy ):
        for i in range(i, len(xs)-1):
            x = 1
        return False
    elif(pntx == 1 and pnty == 1):
        corte.x, corte.y = sx, sy
    elif(pntx == 1):

    elif(pnpty):
    return True
       #xs.insert(len(a)-1,x)
def insertar(xs, ys, corte, xy):
    xs.insert(len(xs)-1,xy.x+corte.width)
    ys.insert(len(ys)-1,xy.y+corte.height)

def cortar(cortado, xs, ys, corte, p):
    if (p>len(xs)):
        return False
    if (not xs[p] and not ys[p]):
        corte.x, corte.y = 0, 0
        insertar(xs[p],ys[p], corte, Punto(0,0))
    else:
        xy = Punto(-1, -1)
        if (verificar(xs[p], ys[p], corte, xy)):
            insertar(xs[p],ys[p], corte, xy)
        else:
            cortar(cortado, xs, ys, corte, p+1)


    return True

def comparator( rectangle ) :
    return rectangle.getArea()

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
    cuts.sort(key = comparator, reverse=True)
    for x in xs:
        x.append(dim[0])
    for y in ys:
        y.append(dim[1])
    cortado = []

    for c in cuts:
        #it's always goin to check the first table for space
        cortar(cortado, xs, ys, c, 0)
        #c.imprimir()

    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == "__main__":
    main()
