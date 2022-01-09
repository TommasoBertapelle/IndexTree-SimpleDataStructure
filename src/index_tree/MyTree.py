from index_tree.NamedTreeNode import NamedTreeNode

try:
    import graphviz
except ModuleNotFoundError:
    print('Module graphviz NOT found, however NOT USEFUL for unit-testing')
#******************TODO******************
#******************TODO******************

class MyTree(object):
    """"""
    def __init__(self, content, nameNode):
        """"""
        #*********TODO*********
        #*********TODO*********        
        if not self.isString(nameNode):
            raise TypeError ('expected <class \'str\'>, got '+str(type(nameNode)))
        
        rootTreeNode = NamedTreeNode(parent   = nameNode, \
                                     child    = [],       \
                                     content  = content,  \
                                     nameNode = nameNode)
                                          
        self.node_dict = {nameNode: rootTreeNode}
        
    def addNode(self, parent, content, nameNode):
        """"""
        #*********TODO*********
        #*********TODO*********
        if not self.isString(parent):
            raise TypeError ('expected <class \'str\'>, got '+str(type(parent)))
            
        if not self.isNodePresent(parent):
            raise TypeError ('node not present')
        
        if not self.isString(nameNode):
            raise TypeError ('expected <class \'str\'>, got '+str(type(nameNode)))
            
        if not self.isValidNameNode(nameNode):
            raise ValueError ('nameNode already present')
        
        self.node_dict[parent].child.append(nameNode)
        
        self.node_dict[nameNode] = NamedTreeNode(parent   = parent,  \
                                                 child    = [],      \
                                                 content  = content, \
                                                 nameNode = nameNode)
                                                 
    def removeNode(self, nameNode):
        """"""
        #*********TODO*********
        # Handle the case when someone wants to delete
        # the root node
        #*********TODO*********
        if not self.isString(nameNode):
            raise TypeError ('expected <class \'str\'>, got '+str(type(nameNode)))
            
        if not self.isNodePresent(nameNode):    #<-- Evaluate if necessary, exploit dict excption
            raise TypeError ('node not present')
            
        if self.isRoot(nameNode):
            raise TypeError ('CANNOT delete the root') #<-- evaluate if TypeError is appropriate
            
        delNode_list = []        
        for child in self.node_dict[nameNode].child:
        
#            print(child)
            
            if self.isLeaf(child):
                delNode_list.append(self.node_dict[child])
#                print(self.node_dict[self.node_dict[child].parent].child)
#                self.node_dict[self.node_dict[child].parent].child.remove(child)
#                print(self.node_dict[self.node_dict[child].parent].child)
                del self.node_dict[child]
                
            else:
                delNode_list.append(self.removeNode(child))
                
        delNode_list.append (self.node_dict[nameNode])
#        print(self.node_dict[self.node_dict[nameNode].parent].child)
        self.node_dict[self.node_dict[nameNode].parent].child.remove(nameNode)
#        print(self.node_dict[self.node_dict[nameNode].parent].child)
#        print(delNode_list)
        del self.node_dict[nameNode]
#        print(delNode_list)
        
        return delNode_list
                                                 
    def getNode(self, nameNode):
        """"""
        if not self.isString(nameNode):
            raise TypeError ('expected <class \'str\'>, got '+str(type(nameNode)))
            
        if not self.isNodePresent(nameNode):    #<-- Evaluate if necessary, exploit dict excption
            raise TypeError ('node not present')
        
        return self.node_dict[nameNode]
        
    def viewTree(self, fileName = 'MyTree.gv'):
        """"""
        g = graphviz.Digraph('G', filename = fileName)
        
        treeNodesEdges_list = []
        for nameNode in self.node_dict.keys():
            
            if self.isLeaf(nameNode):
                break
   
            for childTreeNode in self.node_dict[nameNode].child:
                treeNodesEdges_list.append((nameNode, childTreeNode))
        
        treeNodesEdges_set = set(treeNodesEdges_list) #<-- TODO: remove in the future
        for fromTreeNode, toTreeNode in treeNodesEdges_set:
            g.edge(fromTreeNode, toTreeNode)

        g.view()
        
    #INTERNAL FUNCTIONS
    def isRoot(self, nameNode):
        """"""
        if self.node_dict[nameNode].parent != nameNode:
            return False #node NOT root
            
        return True      #node IS root
        
    def isLeaf(self, nameNode):
        """"""
        if self.node_dict[nameNode].child:
           return False  #node NOT leaf 
        
        return True      #node IS leaf
        
    def isNodePresent(self, nameNode):
        """"""
        if nameNode in self.node_dict.keys():
            return True #node present
        
        return False    #node NOT present
        
    def isString(self, nameNode):
        """"""
        if isinstance(nameNode, str):
            return True
        
        return False
        
    def isValidNameNode(self, nameNode):
        """"""
        if nameNode not in self.node_dict.keys():
            return True #valid node-name
            
        return False    #NOT valid node-name
        
if __name__ == '__main__':
    
    import numpy as np
    from DataContainer import DataContainer
    
    data      = np.random.normal(0, 1, int(1e3))
    dataParam = {'smpRate': 44.1e3, \
                 'pwrLO'  : 17.31e-3} 
    
    test = MyTree(DataContainer(data, dataParam), 'root')
    test.addNode('root', DataContainer(data[0:10], dataParam), 'sx')
    test.addNode('root', DataContainer(data[0:20], dataParam), 'dx')
    test.addNode('sx', DataContainer(data[0:2], dataParam), 'sx_2')
    test.addNode('root', DataContainer(data[0:7], dataParam), 'wer')
    test.addNode('sx', DataContainer(data[0:2], dataParam), 'dx_2')
    test.addNode('dx', DataContainer(data[0:2], dataParam), 'argh')
    
    print(test.isRoot('root'))
    
    print(len(test.getNode('root').content.get_data()))
    print(len(test.getNode('sx').content.get_data()))
    
    test.viewTree()
                                                 
                                                 
                                                 
                                                 
                                                 
