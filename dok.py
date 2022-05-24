from logging import raiseExceptions
from operator import indexOf
from abstract_spars import AbstractSparse
import json
import os
class DokSparse(AbstractSparse):
    ''' DOK Sparse is a sparse matrix implemented by
      python dictionary which is used to:
      #### implement LeetCode project more accurate
    '''
    def __init__(self,rows=0,columns=0):
        super().__init__(rows,columns)
        self.matrix = {}
    def import_json(self,path):
        try:
            with open(path) as json_file:
                data = json.load(json_file)
                self.matrix = dict((key,d[key]) for d in data for key in d)
        except:
            raise Exception("invalid path")

    def size(self):
        return len(self.matrix)
    def insert(self,vertice,connections=[]):
        self.matrix[vertice]=connections
    def remove(self,vertice1,vertice2):
        return self.matrix[vertice1].pop(indexOf(self.matrix[vertice1],vertice2))
    #get similars function
    def get(self,vertice):
        try:
            return self.matrix[vertice]
        except:
            raise Exception("Not Avalable")
    def remove_row(self,row):
        return self.matrix.pop(row)
    def __len__(self):
        return len(self.matrix)


obj  = DokSparse()
obj.import_json('classes/similars.json')
print(obj.get("Two Sum"))
print(obj.remove("Two Sum","4Sum"))
print(obj.remove_row("Two Sum"))
print(len(obj))
print(obj)