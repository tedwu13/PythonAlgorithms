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
    
    #final write to the outputString
    outputString.append(lastChar + str(charCount))
    output = ''.join(outputString)
    
    if len(output) > len(string): 
        return "nothing"
    else:
        return output
    print output
print compressString("aaaabccccccaa")
print compressString("abc")

            