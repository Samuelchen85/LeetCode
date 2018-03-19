class Solution(object):
    def checkSCG(self, target, stack):
        if target in stack:
            self.scg.extend(stack)
            return
        stack.append(target)
        lbs = self.dic[target]
        for lb in lbs:
            self.checkSCG(lb, stack)
        stack.pop()

    def setData(self, graph):
        self.dic = {}
        self.scg = []
        self.graph = graph
        for i in range(0, len(graph)):
            self.dic[i] = graph[i]
        for i in range(0, len(graph)):
            if i in self.scg:
                continue
            self.checkSCG(i, [])

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        self.setData(graph)
        res = []
        for i in range(0, len(graph)):
            if i not in self.scg:
                res.append(i)
        return res
