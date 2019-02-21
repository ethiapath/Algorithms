#!/usr/bin/python

import sys
'''
Return the number of possible ways to make change given an amount and a list of denominations

Keep track of the number of combinations
make a recursive function that takes in a running total
check if the running total is equal to zero
if so increment num_combos and return
else loop through the denominations
check if the denomination does not excede the running total
if so call the recursive func subtracting the denomination from the running total

I need to get the permutations instead of combinations
'''

def making_change(amount, denominations):
  if amount < 1:
    return 1

  class cents:
    num_combo = 0

  def find_change(running_total, combinations):
    if running_total == 0:
    # if running_total == amount:
      cents.num_combo += 1
      print('num_combos: ', cents.num_combo, 'combinations: ', combinations)
      return

    for coin in denominations:
      new_total = running_total - coin
      # if running_total <= amount:
      #   combinations.append(coin)
      #   find_change(coin + running_total, combinations[:])

      if (running_total - coin) >= 0:
        print('coin: ', coin, 'running_total: ', running_total, 'num_combos: ', cents.num_combo)
        combinations.append(coin)
        find_change(running_total - coin, combinations[:])
      else:
        return

  find_change(amount, [])
  return cents.num_combo

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")