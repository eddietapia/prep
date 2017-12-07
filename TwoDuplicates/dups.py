def dups(int_array):
  if int_array is None:
    return None
  table = {}
  for item in int_array:
    if item in table.keys():
      table[item] += 1
    else:
      table[item] = 1

  for item in table:
    if table[item] == 2:
      print item

array = range(20)
array += [10, 14]

dups(array)

