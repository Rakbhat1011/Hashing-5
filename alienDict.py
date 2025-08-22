"""
Create a node for every unique character
For each adjacent word pair, find the first differing char and add a directed edge u - v (u comes before v)
If no diff and w1 is longer than w2, it’s invalid (prefix issue) - return ""
Topological sort (Kahn’s BFS). If we can’t process all nodes (cycle), return ""
"""
"""
Time Complexity: O(T + U) where T is total characters across words, U is number of unique chars
Space Complexity: O(U + E) for nodes and edges
"""


from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
       
        graph = defaultdict(set)  
        indeg = {c: 0 for w in words for c in w} 

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indeg[b] += 1
                    break  

        q = deque([c for c, d in indeg.items() if d == 0])
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return "".join(order) if len(order) == len(indeg) else ""

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))  # "wertf"
print(s.alienOrder(["z","x"]))                        # "zx"
