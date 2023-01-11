'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in 
their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in 
seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back 
to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means 
that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, 
where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

'''

class Solution:
    counts = []
    neighbours = []
    has_apple = []
    def dfs(self, node, parent):
        
        for c in self.neighbours[node]:
            if c == parent:
                continue

            c_count = self.dfs(c, node)

            if c_count > 0:
                self.counts[node] = self.counts[node] + c_count

        if self.counts[node] > 0 or self.has_apple[node]:
            return self.counts[node] + 2

        return 0


    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.counts = [0]*n
        self.has_apple = hasApple
        self.neighbours = [[] for _ in range(0, n)]

        for edge in edges:
            self.neighbours[edge[0]].append(edge[1])
            self.neighbours[edge[1]].append(edge[0])

        self.dfs(0, -1)

        return self.counts[0]
