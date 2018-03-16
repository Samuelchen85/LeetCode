class Solution(object):
    def setData(self, code):
        self.code = code
        self.length = len(code)
        self.indx = 0
        self.stack = []
        self.has_start_tag = False
        self.has_end_tag = False

    def checkTag(self):
        tag_name = ""
        close_tag = False

        # Rule 7, 8
        if self.code[self.indx:].startswith("<![CDATA["):
            find_pos = self.code[self.indx:].find("]]>", 1)
            if find_pos == -1:
                return False
            self.indx += find_pos + 3
            return True

        # Rule 4, 6
        if self.code[self.indx+1] == '/':
            # close tag
            self.indx += 1
            close_tag = True
        self.indx += 1
        while(self.indx<self.length and self.code[self.indx] != '>'):
            ch = self.code[self.indx]
            if ch<'A' or ch>'Z':
                return False
            tag_name += self.code[self.indx]
            self.indx += 1
        if self.indx == self.length:
            return False
        elif len(tag_name) <1 or len(tag_name)>9:
            # Rule 3
            return False
        else:
            if close_tag:
                # Rule 1, 2, 5
                if len(self.stack) == 0:
                    return False
                top_tag = self.stack.pop()
                if top_tag != tag_name:
                    return False
                if len(self.stack) == 0:
                    if self.code.endswith("</" + tag_name + ">"):
                        self.has_end_tag = True
                    else:
                        return False
            else:
                if self.code.startswith("<"+tag_name+">"):
                    self.has_start_tag = True
                self.stack.append(tag_name)
            self.indx += 1
        return True

    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        self.setData(code)
        if self.code[self.indx] != '<':
            return False

        while(self.indx<self.length):
            if self.code[self.indx] == '<':
                if not self.checkTag():
                    return False
            else:
                self.indx += 1
        return self.has_start_tag and self.has_end_tag and len(self.stack) == 0
