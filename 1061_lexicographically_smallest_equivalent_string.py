'''
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are 
equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
'''

from typing import List, Dict, Set
class Solution:
    neighbours: Dict = {}
    node_wise_map: Dict = {}
    visited: Set = set()

    def dfs(self, node):
        for n in self.neighbours[node]:
            if n not in self.visited:
                self.visited.add(n)
                self.dfs(n)


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.neighbours = {}
        self.node_wise_map = {}
        self.visited = set()
        for s1i, s2i in zip(s1, s2):
            if s1i not in self.neighbours:
                self.neighbours[s1i] = []
            if s2i not in self.neighbours:
                self.neighbours[s2i] = []

            self.neighbours[s1i].append(s2i)
            self.neighbours[s2i].append(s1i)

        # Apply DFS
        for key in self.neighbours:
            if key not in self.node_wise_map:
                self.neighbours[key] = list(set(self.neighbours[key]))
                self.visited = set()
                self.dfs(key)
                self.node_wise_map[key] = list(self.visited)
        
        # Get Sorted for each to construct result
        result = ''
        for key in baseStr:
            if key in self.node_wise_map:
                result += sorted(self.node_wise_map[key])[0]
            else:
                result += key

        return result
            
