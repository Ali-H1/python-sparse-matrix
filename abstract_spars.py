from abc import abstractmethod

class AbstractSparse:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    @abstractmethod
    def insert(self ,row, col,value):
        pass
    @abstractmethod
    def remove(self ,row, col):
        pass
    @abstractmethod
    def get(self ,row, col):
        pass
    @abstractmethod
    def show(self):
        pass
    def _binary_search(self, l: list, key: int) -> tuple:
        if l == []:
            return 0, 0
        start = 0
        end = len(l)
        while start < end:
            mid = (start + end) // 2
            if l[mid] > key:
                end = mid
            elif l[mid] == key:
                return mid, 1
            else:
                start = mid
        if l[start] == key:
            return start, 1
        return end, 0

    
class DOKSparse(AbstractSparse):
    def __init__(self, row, col):
        super().__init__(row, col)

class COOSparse(AbstractSparse):
    def __init__(self, row, col):
        super().__init__(row, col)
        
    