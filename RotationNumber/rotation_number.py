def find_rotation(int_array):
  if int_array is None:
    return "Error. Invalid string."
  for index in range(len(int_array) - 1):
    if int_array[index] > int_array[index + 1]:
      return len(int_array) - 1 - index
  return 0

list1 = [2,4,6,8,10]
list2 = [10,2,4,6,8]
list3 = [4,6,8,10,2]

print find_rotation(list1)
print find_rotation(list2)
print find_rotation(list3)

