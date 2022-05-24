from dok import DokSparse
from lil import LILSparse
from coo import CooSparse
import unittest

class TestMethods(unittest.TestCase):
    
    def test_insert(self):
        dok_obj = DokSparse(3,5)
        lil_obj = LILSparse(3,5)
        coo_obj = CooSparse(3,5)
        dok_obj.insert("test insert",["test1","test2","test3"])
        lil_obj.insert(2,3,23)
        coo_obj.insert(2,3,23)
        self.assertEqual(dok_obj.get("test insert"),["test1","test2","test3"],"dok insert" )
        self.assertEqual(coo_obj.get(2,3), 23,"lil insert")
        self.assertEqual(lil_obj.get(2,3), 23,"coo insert")
    def test_remove(self):
        dok_obj = DokSparse(3,5)
        lil_obj = LILSparse(3,5)
        coo_obj = CooSparse(3,5)
        dok_obj.insert("test insert",["test1","test2","test3"])
        lil_obj.insert(2,3,23)
        coo_obj.insert(2,3,23)
        dok_obj.remove("test insert","test1")
        lil_obj.remove(2,3)
        coo_obj.remove(2,3)
        self.assertEqual(dok_obj.get("test insert"),["test2","test3"],"dok remove" )
        self.assertEqual(lil_obj.get(2,3), None,"coo remove")
        self.assertEqual(coo_obj.get(2,3), None,"lil remove")

    def test_length(self):
        dok_obj = DokSparse(3,5)
        lil_obj = LILSparse(3,5)
        coo_obj = CooSparse(3,5)
        dok_obj.insert("test insert",["test1","test2","test3"])
        lil_obj.insert(2,3,23)
        coo_obj.insert(2,3,23)
        self.assertEqual(len(dok_obj),1,"dok size" )
        self.assertEqual(len(lil_obj), 1,"coo size")
        self.assertEqual(len(coo_obj), 1,"lil size")
    def test_array_to_sparse(self):
        lil_obj = LILSparse(3,5)
        coo_obj = CooSparse(3,5)
        lil_obj.array_to_sparse([[0,0,0,4,0],
                                 [2,0,0,0,1],
                                 [0,3,0,3,5]])
        coo_obj.array_to_sparse([[0,0,0,4,0],
                                 [2,0,0,0,1],
                                 [0,3,0,3,5]])
        self.assertEqual(lil_obj.get(0,3), 4,"coo array to sparse")
        self.assertEqual(coo_obj.get(0,3), 4,"lil array to sparse")

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

obj = TestMethods()
obj.test_insert()
obj.test_length()
obj.test_array_to_sparse()
obj.test_remove()