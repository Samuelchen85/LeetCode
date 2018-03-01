

class Solution(object):
    """
    maintain a dictionary, map from: file_content --> [file_path1, ...]
    iterate the dictionary to output the result
    """

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        tree = {}
        for path in paths:
            tks = path.split(" ")
            dir_name = tks[0]
            for i in range(1, len(tks)):
                file_str = tks[i]
                file_items = file_str.split("(")
                file_name = file_items[0]
                content = file_items[1][0:-1]
                full_path = dir_name + "/" + file_name
                if content not in tree:
                    tree[content] = [full_path]
                else:
                    tree[content].append(full_path)
        result = []
        for content in tree:
            if len(tree[content])>1:
                result.append(tree[content])
        return result
