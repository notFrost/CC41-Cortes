from itertools import permutations
class Ccaja:
    def __init__(self, w, h, d, c):
        self.width, self.height,self.depth = w, h, d
        self.pos = (0,0)
        self.sub_cajas = []
        self.weight = 0.0
        self.name = [c]

    def getWeight(self):
        self.weight = 0

    def nothing(self):
        x =2

    def everything(self, other):
        rotations = list(permutations([other.width,other.height,other.depth],3))
        cajas_rotadas = [Ccaja(r[0],r[1],r[2],other.name) for r in rotations]
       #make combinations 
       
    def print(self):
        print(self.width, self.height, self.depth, self.pos, self.name)

def dupla(cajas):
    for i in range(0,len(cajas)-1):
        for j in range(i+1,len(cajas)):
            cajas[i].everything(cajas[j])


def getData(filename):
    #get data from the file 
    lines = [line.rstrip('\n') for line in open(filename, "r") ]

    #get dimensiones
    d = [lines[0].split(" ")[i] for i in range(0,3)]
    #save the cortes dimensions and clean the data for empty spaces
    c = [lines[i].split(" ") for i in range(2,len(lines))]
    #returns number of rectangles 
    return int(lines[1]), d, c

def main():
    import timeit
    start = timeit.default_timer()
    num, dim, cortes = getData("test.txt")
    
    print(num, dim ,cortes)
    
    Cajas = []
    for i in range(num):
        for _ in range(0,int(cortes[i][0])):
            Cajas.append(Ccaja(cortes[i][2],cortes[i][3], cortes[i][4], cortes[i][1]))
    
    dupla(Cajas)

if __name__ == "__main__":
    main()