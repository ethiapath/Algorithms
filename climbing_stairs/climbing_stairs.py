#!/usr/bin/python

import sys

'''
We need to make a function that takes in a number of steps and it needs to return 
the number of ways the stairs can be climbed by 1, 2, or 3 steps at a time

so by using a recursive function that takes in the remaining steps
we can call the function recursivly 
by looping the call passing in 1, 2 and 3
if the remaning_steps doesn't exceed n
decrementing by the number of steps
when the remaining steps is less then zero increment the num_step_combo variable
'''

def climbing_stairs(n, cache=None):
  class steps:
    num_step_combo = 0
  def climb_steps(remaining_steps):
    if remaining_steps <= 0:
      if remaining_steps == 0:
        steps.num_step_combo += 1
      return

    for step in range(1, 4):
      if not remaining_steps - step < 0:
        climb_steps(remaining_steps - step)

  climb_steps(n)
  return steps.num_step_combo


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')