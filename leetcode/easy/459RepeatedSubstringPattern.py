"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
 
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


"""
- Concat the string with itself and remove the first and last characters
- We can do this because we know for sure that the substring would occur at the beginning and end (we concatenated it after all)
- Instead, we drop the first and last to force a check in the middle of the combined string
- If the substring occurs in the middle, we know there is a repeated substring.

Examples:
abc - original
abcabc - concatenated
_bcab_ - drop first and last
abc is not in _bcab_ -> false

abab - original
abababab - concatenated
_bababa_ - drop first and last
abab is in _bababa_ -> true
"""
