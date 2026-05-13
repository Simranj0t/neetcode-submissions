class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        exp_sum = 0
        for i in range(0,len(nums)):
            actual_sum +=nums[i] 
        for i in range(0,len(nums)+1):
            exp_sum += i
    
        return exp_sum - actual_sum