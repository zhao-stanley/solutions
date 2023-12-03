class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = t
        for char in s:
            if char in diff:
                diff = diff.replace(char, "", 1)
        return diff
