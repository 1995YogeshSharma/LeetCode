'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_edges = [0]*(n+1)
        out_edges = [0]*(n+1)

        for edge in trust:
            out_edges[edge[0]] += 1
            in_edges[edge[1]] += 1

        for i in range(1, n+1):
            if out_edges[i] == 0 and in_edges[i] == n-1:
                return i

        return -1
