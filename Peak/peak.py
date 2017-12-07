def findPeak(input):
  """
  Finds the peak of an integer array and returns the index
  of that peak
  """
  if input is None:
    return "Invalid Input"
  for index in range(len(input) - 1):
    if input[index] > input[index + 1]:
      return index
  return len(input) - 1

list1 = [2,4,5,7,10,14]
list2 = [10,7,5,4,3,2,1]
list3 = [2,4,18,5,4,1]

print findPeak(list1)
print findPeak(list2)
print findPeak(list3)

