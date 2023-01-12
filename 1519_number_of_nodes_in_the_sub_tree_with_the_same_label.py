'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
'''

lass Solution:
    ans = []
    children = []
    labels = []

    def dfs(self, node, parent, node_label):
        '''
        Each node returns a list of count for labels, so the counts are propagated bottom up
        '''

        nodecounts = [0]*26
        nodecounts[ord(node_label) - ord('a')] = 1

        for child in self.children[node]:
            if child == parent:
                continue

            childcounts = self.dfs(child, node, self.labels[child])

            for i in range(0, len(childcounts)):
                nodecounts[i] = nodecounts[i] + childcounts[i]

        self.ans[node] = nodecounts[ord(node_label) - ord('a')]

        return nodecounts


    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.children = [[] for _ in range(0, n)]
        self.ans = [0]*n
        self.labels = labels

        for edge in edges:
            self.children[edge[0]].append(edge[1])
            self.children[edge[1]].append(edge[0])

        self.dfs(0, -1, self.labels[0])

        return self.ans

      
