class square:
    sideLength=0
    def __init__(self,sides):
        self.sideLength=sides
    def getLength(self):
        return self.sideLength
    def setLength(self,sides):
        self.sideLength=sides
mySquare=square(5)
print(mySquare.getLength())
mySquare.setLength(10)
print(mySquare.getLength())
