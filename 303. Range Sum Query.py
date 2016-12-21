public class NumArray {
 
    public int[] nums;
 
    public NumArray(int[] nums) {
        this.nums = nums;
    }
 
    public int sumRange(int i, int j) {
        int result = 0;
        for (int counter = i; counter <= j; counter++) {
            result += nums[counter];
        }
        return result;
    }
}
this is java

#sumRange会被调用多次，这样写没效率，会超时


class NumArray(object):
    sums = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums=[0]*len(nums)
        for i in range(0,len(nums)):
            for j in range (0,i+1):
                self.sums[i]+=nums[j]
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i!=0:
            sum = self.sums[j]-self.sums[i-1]
        else:
            sum = self.sums[j]
        return sum
        
     #依然超时