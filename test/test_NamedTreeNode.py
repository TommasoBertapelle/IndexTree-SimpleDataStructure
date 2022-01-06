import unittest

import numpy as np

#*********TODO: installable package*********
from index_tree.DataContainer import DataContainer
from index_tree.NamedTreeNode import NamedTreeNode
#*******************************************

class TestNamedTreeNode(unittest.TestCase):
    """"""
    @classmethod
    def setUpClass(cls):
        """"""
        data      = np.random.normal(0, 1, int(1e3))
        dataParam = {'smpRate': 44.1e3, \
                     'pwrLO'  : 17.31e-3}
        
        cls._namedTreeNode_parent   = 'parentName'
        cls._namedTreeNode_child    = ['child_1', 'child_2', 'child_3']
        cls._namedTreeNode_content  = DataContainer(data, dataParam)
        cls._namedTreeNode_nameNode = 'JohnDoe'
        
        cls._namedTreeNode = NamedTreeNode(parent   = cls._namedTreeNode_parent,  \
                                           child    = cls._namedTreeNode_child,   \
                                           content  = cls._namedTreeNode_content, \
                                           nameNode = cls._namedTreeNode_nameNode)
    
    @classmethod
    def tearDownClass(cls):
        """"""
        pass
        
    def test_parentField(self):
        """"""
        self.assertTrue(__class__._namedTreeNode.parent == __class__._namedTreeNode_parent)
        
    def test_childField(self):
        """"""
        for child in __class__._namedTreeNode.child:
            self.assertTrue(child in __class__._namedTreeNode_child)
            
    def test_contentField(self):
        """"""
        #*********TODO*********
        # - update the test when the issue on DataContainer class method
        #   .get_dataParam() is fixed
        #*********TODO*********
        content_obj = __class__._namedTreeNode.content
        
        self.assertTrue(np.array_equal(content_obj.get_data(), \
                                       __class__._namedTreeNode_content.get_data()))
                                       
        self.assertTrue(content_obj.get_dataParam_keys() == \
                        __class__._namedTreeNode_content.get_dataParam_keys())
        
        for key in __class__._namedTreeNode_content.get_dataParam_keys():
            key_list = [key]
            self.assertTrue(content_obj.get_dataParam(key_list)[key] == \
                            __class__._namedTreeNode_content.get_dataParam(key_list)[key])
                            
    def test_nameNodeField(self):
        """"""
        self.assertTrue(__class__._namedTreeNode.nameNode == \
                        __class__._namedTreeNode_nameNode)
        
        
        
        
