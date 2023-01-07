'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to 
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is 
guaranteed to be unique
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        if we are able to start from some position and circle back. It is a position
        where the value is not negative and the value does not go negative from 
        there on till end.
        At end if the total_sum > 0, that means some solution should exist and since
        we have such value for which the sum did not go negative, that is the solution
        '''
        start_idx = 0
        total_tank = 0
        current_tank = 0
        idx = 0

        for g, c in zip(gas, cost):
            val = g - c

            if current_tank + val < 0:
                start_idx = idx + 1

                current_tank = 0
            else:
                current_tank = current_tank + val

            total_tank = total_tank + val
            idx = idx + 1

        if total_tank < 0:
            return -1

        return start_idx


