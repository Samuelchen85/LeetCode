# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    very straightforward, just pay attention to the case that if the node is a leaf node
    """

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        
        ss = str(t.val)
        if not t.left and not t.right:
            return ss

        if t.left is not None:
            ss += "(" + self.tree2str(t.left) + ")"
        else:
            ss += "()"
        if t.right is not None:
            ss += "(" + self.tree2str(t.right) + ")"
        return ss
