class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        shorter = min(
            word1, word2, key=len
        )  # min/max key parameter allows you to specify a function to differentiate value, pass in len()
        longer = max(word1, word2, key=len)
        for i, _ in enumerate(shorter):
            merged += word1[i] + word2[i]
        merged += longer[len(shorter) :]
        return merged
