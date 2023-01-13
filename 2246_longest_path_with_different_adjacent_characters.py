'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at 
node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed 
array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the 
path have the same character assigned to them.

'''

class Solution:
    len_longest = 1
    children = {}

    def dfs(self, node, labels) -> int:

        longest_children = 0
        second_longest_children = 0

        for i in self.children[node]:

            child_len = self.dfs(i, labels)

            if labels[node] == labels[i]:
                continue

            # print (f'len of child {i} for parent {node} -> {child_len}')

            if child_len >= longest_children:
                second_longest_children = longest_children
                longest_children = child_len

            elif child_len > second_longest_children:
                second_longest_children = child_len

        self.len_longest = max(self.len_longest, longest_children + second_longest_children + 1)

        return longest_children + 1


    def longestPath(self, parent: List[int], s: str) -> int:
        self.children = {i: [] for i in range(0, len(parent))}

        for i in range(0, len(parent)):
            if parent[i] == -1:
                continue
            self.children[parent[i]].append(i)

        # print (f'children {self.children}')

        self.dfs(0, s)

        return self.len_longest
