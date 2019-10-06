#! /usr/bin/python

from functools import reduce
from operator import add

def non_functional():
  people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

  height_total = 0
  height_count = 0
  for person in people:
    if 'height' in person:
      height_total += person['height']
      height_count += 1

  if height_count > 0:
    average_height = height_total / height_count

    print(average_height)
    # => 120

def functional():

  people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

  heights = list(map(lambda p: p['height'],
                 filter(lambda p: 'height' in p, people)))

  if(len(heights) > 0):
    height_total = reduce(add, heights)
    print(height_total / len(heights))

if __name__== "__main__":

  print("Non functional version")
  print("======================")
  non_functional()

  print()
  print("Functional version")
  print("======================")
  functional()

