class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq = {}

        # Initialize all numbers from 0 to n      # nums = [1,2,3]
        for i in range(len(nums) + 1):   # 0,4
            freq[i] = 0 

        # Mark numbers present in nums
        for i in range(len(nums)): #   0,2
            freq[nums[i]] = 1

        # Find missing number
        for k, v in freq.items():
            if v == 0:
                return k