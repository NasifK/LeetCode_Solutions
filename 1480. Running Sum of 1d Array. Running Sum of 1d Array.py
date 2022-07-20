class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        sum = 0
        for num in nums:
            sum += num
            running_sum.append(sum)
            
        return running_sum