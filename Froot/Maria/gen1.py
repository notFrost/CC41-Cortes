# coding=utf-8
class Punto(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

#use id(x) if objects have the same name
class Rect(object):
    def __init__(self, name, h, w):
        self.name = name
        self.width  = w
        self.height = h
        self.rotation = False
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y;
    
    def rotar(self):
        self.width, self.height = self.height, self.width
        rotation = not rotation

    def imprimir(self):
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

def salida():
    return 0

#Iniciation 

class Poblacion:
    def __init__(self):
        self.individuos = []

class Individuo:
    def __init__(self, w, h, n):
        Genes = []


#Evaluation

#Selection

#Crossover

#Mutation

#Termination

#Fit wherever it fits 
def random(n, d, c):
    print (n)

#Genes - 3n
def crearGenes(cortes):
    g = []
    for c in cortes:
        for i in range (0, int(c[3])): 
            g.append(Rect(c[0], int(c[1]), int(c[2])))

    return g

#INTENTO#1---NO FAILURE
#INTENTO#2---Intentar buscar que piezas tienen mismos anchos
#Intento 3 ---- Genetic Algorithm ? 
def main():
    import timeit
    start = timeit.default_timer()

    dim, cortes = [], []
    num = getData("test", dim, cortes)
    genes = crearGenes(cortes)

    for r in genes:
        r.imprimir()

    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == "__main__":
    main()
    