"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

 
Constraints:

	2 <= nums.length <= 10^4
	-10^9 <= nums[i] <= 10^9
	-10^9 <= target <= 10^9
	Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


"""
Most famous/classic LeetCode problem

Make a hashmap that looks like this:

{
    complement: index,
}

for example, if the number is 2 and the target is 9, the complement is 7
if we can find 7 in the hashmap, we can get its index
otherwise, we'll add to the hashmap, with the key being the number and the value being the index
"""
