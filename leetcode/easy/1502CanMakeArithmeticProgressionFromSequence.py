"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
 
Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

 
Constraints:

	2 <= arr.length <= 1000
	-10^6 <= arr[i] <= 10^6

"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedArr = sorted(arr)
        diff = sortedArr[1] - sortedArr[0]
        for i in range(1, len(sortedArr) - 1):
            if sortedArr[i + 1] - sortedArr[i] != diff:
                return False
        return True


"""
Once sorted, an arithmetic arithmetic progression sohuld all have the same differences, so we can set the difference to be between the second and first element.
Then loop through the array with each remaining pair and compare to the difference, if it is different, then it must not be possible.


More compact solution (saves memory by declaring less variables as well):

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedArr = sorted(arr)
        return all(sortedArr[i + 1] - sortedArr[i] == sortedArr[1] - sortedArr[0] for i in range(1, len(sortedArr) - 1))
"""
