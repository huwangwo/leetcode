class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return[]
        else:
            a = [[1]]
            for i in range(1,numRows):
                b = [0]*(len(a[i-1])+1)
                for j in range(len(a[i-1])):
                    b[j]+=a[i-1][j]
                    b[j+1]+=a[i-1][j]
                a.append(b)
            return a
        
        
        
        
        
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int;; rtype: List[List[int]]
        """
        if not numRows: return []
        ret = [[1]]
        numRows -= 1
        while numRows:
            ret.append([1] + [a+b for a,b in zip(ret[-1][:-1], ret[-1][1:])] +[1])
            numRows-=1
        return ret
            
            
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
    
    
    
class Solution:
    def generate(self, numRows):
        return map(lambda m: reduce(lambda r, n: r + [r[-1] * (m - n) / (n + 1)], xrange(m), [1]), xrange(numRows))