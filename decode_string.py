
# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
        
def stacky(s):
    """
    When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
    push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
    the enclosed string k times.
    """
    stack = []
    current_string = ""
    k = 0
    
    for char in s:
        if char == "[":
            # Just finished parsing this k, save current string and k for when we pop
            stack.append((current_string, k))
            # Reset current_string and k for this new frame
            current_string = ""
            k = 0
        elif char == "]":
            # We have completed this frame, get the last current_string and k from when the frame 
            # opened, which is the k we need to duplicate the current current_string by
            last_string, last_k = stack.pop()
            current_string = last_string + last_k * current_string
        elif char.isdigit():
            k = k * 10 + int(char)
        else:
            current_string += char
    
    return current_string