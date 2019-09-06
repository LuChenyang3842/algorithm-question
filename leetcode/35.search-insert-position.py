#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if  i>0 and target >= nums[i-1] and target <= nums[i]:
                return i
            # if taget > nums[i]:
            #     return i


        

