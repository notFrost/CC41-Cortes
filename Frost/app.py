import random
bigList = []


def first(iteration, n, blockList, rotation, point):
    global bigList
    if n < 3:
        iteration.checkO(blockList.first, rotation, point)
        del blockList[0]
        n += 1
        first(iteration, n, blockList, False, 0)
        first(iteration, n, blockList, False, 1)
        first(iteration, n, blockList, True, 0)
        first(iteration, n, blockList, True, 1)

    else:
        bigList.append(iteration)


class cBlock:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.x = 0
        self.y = 0

    def rotate(self):
        self.width, self.height = self.height, self.width


class cIteration:
    def _init_(self, canvas):
        self.list = []
        self.width = canvas.width
        self.heigh = canvas.height

    def checkO(self, block, rotation, orientation):
        comingsoon = True


def compare(thing):
    return thing.area


def orderList(List):
    List.sort(key=compare, reverse=True)


def createList():
    blockList = []
    for i in range(random.randint(5, 10)):
        blockList.append(
            cBlock(5*random.randint(1, 50), 5*random.randint(1, 50)))
    return blockList


def main():
    n = 0
    Canvas = cBlock(50*random.randint(5, 15), 50*random.randint(5, 15))
    blockList = createList()
    for x in range(len(blockList)):
        print(blockList[x].height, blockList[x].width)

    orderList(blockList)

    for x in range(len(blockList)):
        print(blockList[x].height, blockList[x].width)
    firstIteration = secondIteration = cIteration(Canvas)
    firstIteration.list.append()


main()
