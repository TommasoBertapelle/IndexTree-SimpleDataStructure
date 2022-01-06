import unittest

import numpy as np

#*********TODO: installable package*********
from index_tree.DataContainer import DataContainer
#*******************************************

class TestDataContainerException(unittest.TestCase):
    """"""
    def setUp(self):
        """"""
        self.data = list(range(0, int(1e2)))
        self.dataParam = [('smpRate', 44.1e3), \
                          ('pwrLO', 17.31e-3)]
        
    def tearDown(self):
        """"""
        pass
        
    def test_dataTypeException(self):
        """"""
        self.assertRaises(TypeError, DataContainer, self.data, self.dataParam)
        
    def test_dataParamTypeException(self):
        """"""
        data = np.asarray(self.data) #ndarray type convertion, reach the dataParam exception
        self.assertRaises(TypeError, DataContainer, data, self.dataParam)
        
        
