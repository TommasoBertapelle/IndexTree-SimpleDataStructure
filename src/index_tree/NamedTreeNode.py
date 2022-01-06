from index_tree.TreeNode import TreeNode

class NamedTreeNode(TreeNode):
    """"""
    def __init__(self, parent, child, content, nameNode):
        """"""
        super().__init__(parent, child, content)
        self.nameNode = nameNode
