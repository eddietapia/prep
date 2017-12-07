def remove_item(input, item):
  output = []
  counter = 0
  for number in input:
    if number != item:
      output.append(number)
      counter += 1
  print "New Length:", counter 
  return output

    

array = [4,1,1,2,1,3]
print remove_item(array, 1)



