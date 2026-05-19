class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None]*capacity
        self.capacity = capacity

    def getIndexOfElement(self, n:int):
        for i,num in enumerate(self.arr):
            if num == n:
                return i
        return None

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        s=self.getSize()
        c=self.getCapacity()
        print(f'before pb {self.arr}')
        if s == c:
            self.resize()
        self.arr[self.getSize()]=n
        print(f'pb {self.arr}')

    def popback(self) -> int:
        indexOfLastElement = self.getSize()-1
        element = self.arr[indexOfLastElement]
        self.arr[indexOfLastElement]=None
        return element

    def resize(self) -> None:
        size = self.getCapacity()
        for _ in range(size):
            self.arr.append(None)

    def getSize(self) -> int:
        sizeCount = 0
        for i, n in enumerate(self.arr):
            if self.arr[i] != None:
                sizeCount+=1
        return sizeCount
    
    def getCapacity(self) -> int:
        capCount = 0
        for i in self.arr:
            capCount+=1
        return capCount
