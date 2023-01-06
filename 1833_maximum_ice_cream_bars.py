'''
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

 
'''

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
      '''
      sort the costs and pick till coins are consumed.
      Only concern would be if removing last coin would allow two more coins to be added. This is not possible
        because costs[i+1] > costs[i] (sorted), if we are not able to fit costs[i+1], we definitely cannot fit
        costs[i+2] by removing costs[i]
      '''
      costs = sorted(costs)

      count = 0
      for i in costs:
          coins = coins - i
          if coins >= 0:
              count += 1
      return count
