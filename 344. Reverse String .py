#超时
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ""
        for i in range(1,len(s)+1):
            a = a+s[-i]
        return a
        
#accepted
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        for i in range(0,len(a)/2):
            a[i],a[-i-1] = a[-i-1],a[i]
        return "".join(a)