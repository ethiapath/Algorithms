#!/usr/bin/python

import argparse

'''
finding max profits by buying first and selling later
takes in a list of numbers representing prices
the max profit is going to be max_price - low_price

if I step through the array keeping track of the lowest price I find
and subtracting it from the max price then keep track of which max prices
are the largest I should get the max profit possible

buy_price = low_price
sell_price = max_price

ok so my inital solution works for the first test set
but not for the second set where there's no way to make a profit
I don't think my solution really takes into account the fact that 
you have to buy before you sell

so if I walk through the list when I find a lower buy price and then if that 
is able to find a higher profit then set those values

looking at the second test case the problem is really find max profit or find least losses
So if 

set low_price and max_price to first index
loop through prices
when a lower buy price is found 
loop through the rest of the list
check if a greater profit can be found 
if so set low_price to the new buy price and set max_price to the new sell price
repeat until len(arr)-1
'''

'''
[10, 7, 5, 8, 11, 9]), 6)
[100, 90, 80, 50, 20, 10]), -10)
[1050, 270, 1540, 3800, 2]), 3530)
[100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)
'''

import argparse

def find_max_profit(prices):
  print('=======Start=======')
  low_price = prices[0]
  profit = prices[1] - low_price

  for current in prices[1:]:
    print('profit: ', profit, 'low_price: ', low_price)
    profit = max(current - low_price, profit)
    low_price = min(current, low_price)

  return profit #- low_price

# print(find_max_profit([1050, 270, 1540, 3800, 2]))

'''
  for p in range(2, len(prices)-1):
    print(p, ': ', low_price, max_price)
    if prices[p] < low_price:
      for i in range(p, len(prices)):
        if max_price - low_price < prices[i] - low_price:
          print(max_price - low_price, ' < ', prices[i] - low_price)
          low_price = prices[p]
          max_price = prices[i]
'''
  #return max_price - low_price 
'''
def find_max_profit(prices):
  pass      low_price = max_price = prices[0]

   for p in prices:

     if p < low_price:
      low_price = p
      if max_price - low_price < p - low_price:
        max_price = p
    #if sell_price - p > sell_price - buy_price:

   return max_price - low_price 
'''

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))