class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = num%9
        if num == 0:
            return 0
        elif a==0:
            return 9
        else:
            return a
            
        
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num-1)%9+1