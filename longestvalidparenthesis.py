def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    my_stack = []
    counter = 0
    maximum = 0
    # Iterate through every letter in that string
    for letter in s:
        # Check if it is a valid input
        if letter != "(" and letter != ")":
            print "Error invalid input"
        elif letter == "(":
            my_stack.append("(")
        else:
            # If the stack is empty, there is nothing to pop and we reset the counter
            if len(my_stack) == 0:
                counter = 0
            else:
                my_stack.pop()
                counter += 2
                if len(my_stack) == 0:
                    if counter > maximum:
                        maximum = counter
    difference = counter - maximum
    if len(my_stack) > 0 and difference > maximum:
        maximum = difference
    
    return maximum
