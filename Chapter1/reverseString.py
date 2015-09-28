def reverseString(string):
    output = []
    for i in range(len(string)-1, -1, -1):
        output.append(string[i])
    return ''.join(output)
        
print reverseString("hey")
#expected output should be yeh