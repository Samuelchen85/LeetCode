class MagicDictionary(object):
    """
    A very simple way is just iterate the whole list to compare the given word with all the words in the list
    A more efficient way is to build a hashmap, the key is the length of different given words
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dt = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for ss in dict:
            if len(ss) not in self.dt:
                self.dt[len(ss)] = []
            self.dt[len(ss)].append(ss)
        
    def checkWords(self, w, word):
        if len(w) != len(word):
            return False
        not_equal_count = 0
        for i in range(0, len(w)):
            if w[i] != word[i]:
                not_equal_count +=1
        return not_equal_count==1
            
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if len(word) not in self.dt:
            return False
        wlist = self.dt[len(word)]
        for w in wlist:
            if self.checkWords(w, word):
                return True
        return False
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
