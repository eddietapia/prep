def makeWave(input):
  if input is None:
    return "Input is invalid"
  length = len(input)
  if length <= 1:
    return input
  counter = 0
  output = []
  while length - counter > 1:
    output.append(input[counter + 1])
    output.append(input[counter])
    counter += 2
  if length  - counter == 1:
    output.append(input[counter])

  return output

input = [1,2,3,4]
print makeWave(input)
