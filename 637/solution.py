# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Maintain a map: 
    level index 0 --> [val1, val2, ...]
    level index 1 --> [val1, val2, ...]
    ...
    
    Then just iterate the levels and calculate the average value
    """

    def __init__(self):
        self.lm = {}
        self.level = 0
        
    def checkNodes(self, root):
        if not root:
            return 0
        self.level += 1
        if self.level not in self.lm:
            self.lm[self.level] = []
        self.lm[self.level].append(root.val)
        if root.left:
            self.averageOfLevels(root.left)
        if root.right:
            self.averageOfLevels(root.right)
        self.level -= 1
    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.checkNodes(root)
        res = []
        for i in range(1, len(self.lm.keys())+1):
            level_vals = self.lm[i]
            sum_val = sum(level_vals)
            length = len(level_vals)
            if sum_val%length == 0:
                ave_val = sum_val/length
            else:
                ave_val = sum_val/float(length)
            res.append(ave_val)
        return res
