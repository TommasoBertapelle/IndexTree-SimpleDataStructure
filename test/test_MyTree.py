import unittest

import numpy as np

#*********TODO: installable package*********
from index_tree.MyTree import MyTree
from index_tree.DataContainer import DataContainer
#*******************************************

#************************************
#Remove TreeNode Name with Node Name
#Continue the tests
#************************************

class TestMyTree(unittest.TestCase):
    """"""
    def setUp(self):
        """"""
        self.data      = np.random.normal(0, 1, int(1e3))
        self.dataParam = {'smpRate': 44.1e3, \
                          'pwrLO'  : 17.31e-3}
        
        self.rootNameNode  = 'root'        
        rootNamedTreeNode  = DataContainer(self.data, self.dataParam)
        
        self.dataNamedTree = MyTree(content  = rootNamedTreeNode, \
                                    nameNode = self.rootNameNode)
                                    
    def tearDown(self):
        """"""
        pass
                                    
    def test_MyTreeConstructor(self):
        """
         Initialisation myTree(), checking root-node properties:
          
          1. .child field empty list
          2. .parent field and root-node-name are equal
          3. .content field actually contains what requested
          4. .nameNode field contains the expected name
          
          5. minor checks if present
        """
        root_obj = self.dataNamedTree.node_dict[self.rootNameNode]
        
        #*********************************************************
        # Check if results are what expected
        #*********************************************************
        self.assertTrue(root_obj.nameNode == self.rootNameNode) # 2.
        self.assertTrue(not bool(root_obj.child))               # 1.
        self.assertTrue(root_obj.parent == self.rootNameNode)   # 4. 
        
        self.assertTrue(np.array_equal(root_obj.content.get_data(), self.data))         # 3.
        self.assertTrue(root_obj.content.get_dataParam_keys() == self.dataParam.keys()) # 3.        
    def test_addNode(self):
        """
         Adding new node, checking if:
         
          1. new-node .parent field correctly updated
          2. parent's .child field correctly updated
          
          3. minor checks if presents
        """
        parentNodeName = self.rootNameNode
        newNodeName    = 'lvl1_n1'
        
        data_lvl1_n1      = np.random.normal(0, 1, int(1e3))
        dataParam_lvl1_n1 = {'smpRate': 31.7e3, \
                             'pwrLO'  : 19.13e-3}
        
        self.dataNamedTree.addNode(parent   = parentNodeName,                   \
                                   content  = DataContainer(data_lvl1_n1,       \
                                                            dataParam_lvl1_n1), \
                                   nameNode = newNodeName)
                                        
        parentNodeTree_obj = self.dataNamedTree.node_dict[parentNodeName]
        newTreeNode_obj    = self.dataNamedTree.node_dict[newNodeName]
        
        #*********************************************************
        # Check if results are what expected
        #*********************************************************
        self.assertTrue(newTreeNode_obj.parent == parentNodeName) # 1.
        self.assertTrue(newNodeName in parentNodeTree_obj.child)  # 2.
        
        self.assertTrue(np.array_equal(newTreeNode_obj.content.get_data(), \
                                       data_lvl1_n1)) # 3.
        self.assertTrue(newTreeNode_obj.content.get_dataParam_keys() == dataParam_lvl1_n1.keys()) # 3.
        
    def test_getNode(self):
        """
         To test the .getNode() function, the root node is gathered when MyTree object
         is initialised, hence performing same test of test_MyTreeConstructor(self)
        """
        rqNodeName = self.rootNameNode
        rqNode     = self.dataNamedTree.getNode(rqNodeName)
        
        #*********************************************************
        # Check if results are what expected
        #*********************************************************
        self.assertTrue(rqNode.nameNode == rqNodeName)
        self.assertTrue(rqNode.parent == rqNodeName)
        self.assertTrue(not bool(rqNode.child))
        
        self.assertTrue(np.array_equal(rqNode.content.get_data(), \
                                       self.data))
        self.assertTrue(rqNode.content.get_dataParam_keys() == self.dataParam.keys())
        

    
    

