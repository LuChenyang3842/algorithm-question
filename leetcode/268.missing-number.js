/*
 * @lc app=leetcode id=268 lang=javascript
 *
 * [268] Missing Number
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort(function(a, b){return a-b})
    for(var i =0; i < nums.length; i++){
        if (nums[i] != i){
            return i
        }
    }
    return nums[nums.length-1] + 1
    
};

