#!/usr/bin/python

import math


'''
looking at this problem I can see that division will be
a key component

I should just be able to loop through the keys and do
recipe[key] / ingredients[key] to find how many batches
I can make
That will be the inital check
then I'd need to keep track of the lowest result to find the
maximum numer of batchs possible
then 
no need to keep track of remainder
forgot edge case: what if you're missing an ingredient 


this solution is somewhat efficent since it's necessary to compare every ingredient 
to make sure there is enough to make a batch.
making it O(n) or constant time.

some improvements could include reducing the nested if statments to make
the solution more readable
'''

def recipe_batches(recipe, ingredients):
  lowest_amount = 10000000
  for key in recipe.keys():
    if not ingredients.__contains__(key):
      return 0
    possible_batches = ingredients[key] // recipe[key]
    if possible_batches >= 1:
      if possible_batches < lowest_amount:
        lowest_amount = possible_batches
    else:
      return 0

  return lowest_amount

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs

  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))