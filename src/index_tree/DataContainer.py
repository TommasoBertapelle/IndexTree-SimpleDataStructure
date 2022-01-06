from numpy import ndarray

import warnings

class DataContainer(object):
    """"""
    def __init__(self, data, dataParam_dict):
        """"""
        if not isinstance(data, ndarray):
            raise TypeError ('expected <class \'numpy.ndarray\'>, got '+str(type(data)))
        self.data = data           #<-- TODO check if ndarray
        
        if not isinstance(dataParam_dict, dict):
            raise TypeError ('expected <class \'dict\'>, got '+str(type(dataParam_dict)))
        self.dataParam_dict = dataParam_dict
        
    def get_data(self):
        """"""
        return self.data
        
    def get_dataParam_keys(self):
        """"""
        #*********TODO*********
        # - return dict_keys or list?
        #*********TODO*********
        return self.dataParam_dict.keys()
        
    def get_dataParam(self, rqParamKeys_list):
        """"""
        #*********TODO*********
        # - decide how to handle rqParamKeys_list = []
        # - handle when given a single key, now we are requesting an iterable
        #*********TODO*********
        rqParam_dict = {rqKey:self.dataParam_dict[rqKey] \
                        for rqKey in rqParamKeys_list    \
                        if rqKey in self.get_dataParam_keys()}
        
        return rqParam_dict    
    
    
