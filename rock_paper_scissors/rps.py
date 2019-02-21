#!/usr/bin/python

import sys

'''
how to find permutations
permutations

given a sequence find the unique permutations of
the sequence

start at index
call function with that index added and rest of list
return 'a' + per(list[1:])

declare output arr
create recursive function
pass in num rounds and empty array
check if rounds is 0 for base case
if so add game to games, return
iterate through the choices
call function with rounds decremented 
and current choice added to array passed in previously 
repeat

'''

def rock_paper_scissors(n):
  if n <= 0:
    return [[]]
  games = []
  choices = ['rock', 'paper', 'scissors']

  def permutation(rounds, play):
    # print('rounds: ', rounds,'play: ', play)
    if rounds <= 0:
      games.append(play)
      return
    for i in range(0, len(choices)):
      permutation(rounds-1, play[:] + [choices[i]])

  # games = 
  permutation(n, [])
  # games = combinations_with_replacement('rps', n)
  return games

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')