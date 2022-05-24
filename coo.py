from abstract_spars import AbstractSparse

class CooSparse(AbstractSparse):
    ''' Cordinated sparse matrix is implemented by 3 lists containing:
        rows , columns , values. 
        this is the most common way to implement sparse matrix '''
    def __init__(self,row,col):
        super().__init__(row,col)
        self.rows=[]
        self.cols=[]
        self.data=[]
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
        pos, is_exist = self.coo_binary_search(self.rows.copy(), self.cols.copy(),row,col)
        if is_exist:
            self.data[pos] = value
        else:
            self.rows.insert(pos, row)
            self.cols.insert(pos, col)
            self.data.insert(pos, value)
    #binary search specialized for coo sparse :
    # if key is found but the row value is not correct , 
    # then remove the key index and continue searching for another key
    def coo_binary_search(self, l1: list,l2:list, key: int,keycol:int) -> tuple:
        if l1 == [] or l2 ==[]:
            return 0, 0
        start = 0
        end = len(l1)
        while start < end:
            mid = (start + end) // 2
            if l1[mid] > key:
                end = mid
            elif l1[mid] == key:
                return mid, 1
            else:
                start = mid
        if l1[start] == key:
            if l2[start] == keycol:
                return start, 1
            else:
                l1.pop(start)
                start-=1
        return end, 0
    def remove(self,row,col):
        if self.is_valid_col(col) and self.is_valid_row(row):
            pass
        else:
            raise Exception("Invalid index")
        pos, is_exist = self.coo_binary_search(self.rows.copy(), self.cols.copy(),row,col)
        self.rows.pop(pos)
        self.cols.pop(pos)
        self.data.pop(pos)
    def get(self,row,col):
        if self.is_valid_col(col) and self.is_valid_row(row):
            pass
        else:
            raise Exception("Invalid index")
            return None
        pos, is_exist = self.coo_binary_search(self.rows.copy(), self.cols.copy(),row,col)
        if is_exist:
            return self.data[pos]
        else:
            raise Exception("value is zero")
    def size(self):
        return len(self.data)
    def __len__(self):
        return self.size()
    def array_to_sparse(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]!= 0 :
                    self.rows.insert(i)
                    self.cols.insert(j)
                    self.data.insert(arr[i][j])


        