#! /bin/python

def zero(s):
  if s[0] == "0":
    return s[1:]

def one(s):
  if s[0] == "1":
    return s[1:]

def non_functional():

  def rule_sequence(s, rules):
    for rule in rules:
      s = rule(s)
      if s == None:
        break

    return s

  print(rule_sequence('0101', [zero, one, zero]))
  # => 1

  print(rule_sequence('0101', [zero, zero]))
  # => None

def recursive():

  def rule_sequence(s, rules):

    if(s == None or not rules):
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])

  print(rule_sequence('0101', [zero, one, zero]))
  # => 1

  print(rule_sequence('0101', [zero, zero]))
  # => None

if __name__== "__main__":

  print("Non functional version")
  print("======================")
  non_functional()

  print()
  print("Recursive version")
  print("======================")
  recursive()
