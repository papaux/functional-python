

def non_functional():
  names = ['Mary', 'Isla', 'Sam']

  for i in range(len(names)):
    names[i] = hash(names[i])

  print(names)
  # => [6306819796133686941, 8135353348168144921, -1228887169324443034]

def functional():
  names = ['Mary', 'Isla', 'Sam']
  
  hashes = list(map(hash, names))
  print(hashes)

if __name__== "__main__":

  print("Non functional version")
  print("======================")
  non_functional()

  print()
  print("Functional version")
  print("======================")
  functional()


