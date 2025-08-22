"""
Map each character to its rank in the alien alphabet
Check every adjacent pair (w1, w2) is non-decreasing under that order
Edge case: if w2 is a prefix of w1, it’s invalid
"""
"""
Time Complexity: O(T) where T = total characters across all words
Space Complexity: O(1) (rank map is fixed size 26)
"""


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}

        def in_order(a: str, b: str) -> bool:
            for ca, cb in zip(a, b):
                if ca != cb:
                    return rank[ca] < rank[cb]
            return len(a) <= len(b)

        return all(in_order(words[i], words[i+1]) for i in range(len(words)-1))

s = Solution()
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False

