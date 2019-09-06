#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_to_now = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i]+ sum_to_now >= nums[i]:
                sum_to_now = nums[i]+ sum_to_now
            else:
                sum_to_now = nums[i]
            if sum_to_now > result:
                result = sum_to_now
        return result
            

        

