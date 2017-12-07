def is_invalid_string(S):
  # Perform checks to make sure it is a valid string
  if isinstance(S, str):
    return False
  return True


def is_invalid_set(D):
  # Performs checks to make sure it is a valid set of words
  if isinstance(D, set):
    return False
  return True


def findLongestSubstring(S, D):
  if is_invalid_string(S):
    return "No substring found"
  if is_invalid_set(D):
    return "No substring found"
  stringDict = {}
  # Parse the string to find the words and indices
  for i in range(len(S)):
    letter = S[i]
    if letter in stringDict.keys():
      stringDict[letter] += [i]
    else:
      stringDict[letter] = [i]
  
  longestSubstring = ""

  # Iterate through the set of words
  for word in D:
    current_index = -1
    flag = False
    for letter in word:
      if letter not in stringDict.keys():
        break;
      else:
        for j in range(len(stringDict[letter])):
          index = stringDict[letter][j]
          if index > current_index and index < len(S):
            current_index = index
            # Check if the last character was in the dictionary
            if j == len(stringDict[letter])-1:
              flag = True
          else:
            flag = False
            

    if flag and len(word) > len(longestSubstring):
      longestSubstring = word
  if longestSubstring == "":
    return "No substring found"
  return longestSubstring
      
      

S = "abppplee"
D = {'able', 'ale', 'apple', 'bale', 'kangaroo'}
S2 = "wagggtermelon"
D2 = {'water', 'watermel', 'watermelon', 'melon'}
"""
What if S is invalid? Return 
assert (findLongestSubstring(45, {}),'No substring found')
How big can S be?
how many words can d contain? 
How long can a word in d be? 
Are they all lowercase characters? is A the same as a?
will d never be sorted?
Test cases:
S is larger than d
word in d is larger than s
multiple longest substrings
no valid substrings
substring at the end of S when S is huge
"""
print findLongestSubstring(S, D)
print findLongestSubstring(45, {})
print findLongestSubstring('tree', {'treeeee', 'treeeeeeeeeee'})
print findLongestSubstring(S2, D2)

assert (findLongestSubstring(45, {}),'No substring found')
assert (findLongestSubstring('tree', {'treeeee', 'treeeeeeeeeee'}),'No substring found')
assert (findLongestSubstring(S2, D2),'watermelon')


