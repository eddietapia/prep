import re

global list

def find(word, input):
    global list
    # Check if the input is valid
    if word is None or input is None:
        return
    # Check if there are valid substring inside our word
    for item in input:
        if word in item and (re.sub(word, '', item) != ""):
	    if word not in list:
	        list.append(word)
	    re.sub(word, '', item)

def simplewords(input):
    global list
    list = []
    for item in input:
        find(item, input)
    return list
        


#input = ['snap', 'chat', 'snapchat', 'ever', 'salesperson', 'per', 'person', 'sales', 'son', 'whatsoever', 'what', 'so']
input = ['a', 'b', 'c', 'd', 'ab', 'az', 'de', 'add', 'dead', 'added']
value = simplewords(input)
print 'Items returned: ', len(value)
print value
