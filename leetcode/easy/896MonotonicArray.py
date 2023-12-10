"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
 
Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

 
Constraints:

	1 <= nums.length <= 10^5
	-10^5 <= nums[i] <= 10^5

"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] > nums[0]:  # if true, implies increasing order
            for i in range(len(nums) - 1):
                if (
                    nums[i] > nums[i + 1]
                ):  # if a number is greater than the next, return false
                    return False
            return True
        else:  # if true, implies decreasing order
            for i in range(len(nums) - 1):
                if (
                    nums[i] < nums[i + 1]
                ):  # if a number is smaller than the next, return false
                    return False
            return True


"""Intuitive Solution (not very efficient)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = sorted(nums)
        dec = sorted(nums, reverse=True)

        return nums == inc or nums == dec
"""
