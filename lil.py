from logging import exception
from abstract_spars import AbstractSparse

class LILSparse(AbstractSparse):
    ''' Sparse matrix implemented by list in lists which contains 
        2 sets of lists ; one having the row elements and the other
        one storing the nonzero elements column
    '''
    def __init__(self, row, col):
        super().__init__(row, col)
        self.data =[]
        self.column=[]
        for _ in range(self.row):
            self.data.append([])
            self.column.append([])

    def is_valid_row(self, row):
        if 0 <= row < self.row:
            return True
        return False

    def is_valid_col(self, col):
        if 0 <= col < self.col:
            return True
        return False


    def insert(self , row ,col,value):
        if self.is_valid_col(col) and self.is_valid_row(row):
            pass
        else:
            raise Exception("Invalid index")
        data = self.data[row]
        row = self.column[row]
        pos, is_exist = self._binary_search(row, col)
        if is_exist:
            row[pos] = col
            data[pos] = value
        else:
            row.insert(pos, col)
            data.insert(pos, value)

    def remove(self,row,col):
        index = self.column[row].index(col)
        self.data[row].pop(index)
        self.column[row].pop(index)
    
    def get(self,row,col):
        try:
            index  = self.column[row].index(col)
            return self.data[row][index]
        except:
            raise Exception("not avalable")
    def size(self):
        length = 0
        for i in range (self.row):
            length += len(self.data[i])
        return length
    def __len__(self):
        return self.size() 
    def array_to_sparse(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]!= 0 :
                    self.insert(i,j,arr[i][j])
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

        