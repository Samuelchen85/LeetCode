class Solution(object):
    """
    aaa
       bbbbb
          cccc.txt
          dd.png
       eeeeeeeeeeee
       fffffff
          ggggggggggggg.txt

    It's more like a tree structure, we iterate each line above to update a "tree" (we do not really need to build the tree, but suppose there's a tree structure), 
    in the self.tree, we only keep the latest path in the "tree"
    whenever we find a file, we call self.updateMaxLength to update the maximum file length
    """

    def __init__(self):
        self.ml = 0
        self.tree = {}
    
    def updateMaxLength(self, depth, path_name):
        length = 0
        for i in range(1, depth):
            length += self.tree[i]
        length += len(path_name)
        if length > self.ml:
            self.ml = length
    
    def lengthLongestPath(self, ss):
        """
        :type input: str
        :rtype: int
        """
        prev_depth = 0
        tks = ss.split("\n")
        for i in range(0, len(tks)):
            phs = tks[i]
            lvs = phs.split("\t")
            depth = len(lvs)
            path_name = lvs[-1]
            if "." in path_name:
                self.tree[depth] = len(path_name)
                self.updateMaxLength(depth, path_name)
            else:
                self.tree[depth] = len(path_name) + 1
        return self.ml
