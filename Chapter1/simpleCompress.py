def compressString(string): 
    outputString = []
    lastChar = ''
    charCount = 1
    
    for char in string:
        if char == lastChar:
            charCount += 1
        else:
            if lastChar != '':
                outputString.append(lastChar + str(charCount))
                charCount = 1
        lastChar = char
    
    #final write
    outputString.append(lastChar + str(charCount))
    output = ''.join(outputString)
    
    if len(output) > len(string): 
        return "nothing"
    else:
        return output
    print output
print compressString("aaaabccccccaa")
print compressString("abc")

#print a4b1c6a2
#print a1b1c1
            