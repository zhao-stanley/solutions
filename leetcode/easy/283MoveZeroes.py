"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] != 0:
                left += 1

"""
- Use two pointers, use left pointer to keep track of element to replace
- Think about moving all non-zero elements to the left
- We iterate with our right pointer, if the number at the right pointer is non-zero, we swap with our left pointer
- Our left pointer will always be on a zero, because if it isn't, we iterate it until it is at a zero
- Once we encounter a non-zero, we swap it with the left pointer
"""
