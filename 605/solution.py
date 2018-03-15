class Solution(object):
    """
    The key thing is thinking about the corner cases
    """
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        i=0
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 0 and n==1:
                return True
            else:
                return False
        while(i<length and n>0):
            if i==0:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            elif i == length-1:
                if flowerbed[i] == 0 and flowerbed[i-1]==0:
                    n -= 1
                i += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
        if n<=0:
            return True
        return False

