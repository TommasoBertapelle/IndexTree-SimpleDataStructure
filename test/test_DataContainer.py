import unittest

import numpy as np

from itertools import chain, combinations

#*******************************************
from index_tree.DataContainer import DataContainer
#*******************************************

class TestDataContainer(unittest.TestCase):
    """"""
    def setUp(self):
        """"""
        self.data      = np.random.normal(0, 1, int(1e3))
        self.dataParam = {'smpRate': 44.1e3, \
                          'pwrLO':   17.31e-3}
        
        self.dataContainer_obj = DataContainer(self.data, self.dataParam)
    
    def tearDown(self):
        """"""
        pass
    
    def test_get_data(self):
        """"""
        self.assertTrue(np.array_equal(self.data, self.dataContainer_obj.get_data()))
        
    def test_get_dataParam_Keys(self):
        """"""
        self.assertTrue(self.dataContainer_obj.get_dataParam_keys() == self.dataParam.keys())
        
    def test_get_dataParam_subset(self):
        """"""
        dataParamKeys_subSet = chain.from_iterable(combinations(self.dataParam.keys(), r) \
                                                   for r in range(1, len(self.dataParam.keys())+1))
        
        #*********************************************************
        # Check if results are what expected
        #*********************************************************        
        for rqParamKeys_list in dataParamKeys_subSet:
            dataParamCtrl_dict = {key: self.dataParam[key] \
                                  for key in rqParamKeys_list}
                                  
            self.assertTrue(self.dataContainer_obj.get_dataParam(rqParamKeys_list) == dataParamCtrl_dict)
            
    def test_get_dataParam_intersec(self):
        """"""
        rqParamKeys_list = ['smpRate', 'pwrLO', 'uselessKey']
        
        dataParamCtrl_dict = {key: self.dataParam[key]    \
                              for key in rqParamKeys_list \
                              if key in self.dataParam.keys()}
        
        #*********************************************************
        # Check if results are what expected
        #*********************************************************                     
        self.assertTrue(self.dataContainer_obj.get_dataParam(rqParamKeys_list) == dataParamCtrl_dict)
        
        
        
        
        
