#uniqueChar.py

#Implement an algorithm that would determine if string has all unique characters

def isUniqueChar1(inputString):
    sortString = ''.join(sorted(inputString))
    for i in range(0, len(inputString)):
        if sortString[i] == sortString[i+1]:
            return False
        else:
            return True

def isUniqueChar2(inputString):
    charList = []
    for char in inputString:
        if char in charList:
            return False
        else:
            charList.append(char)

def isUniqueChar3(inputString):
    # the reason why you want to use ord(char) is to conver "A" to 95
    if len(inputString) > 256:
        return False
    else:
        charList = [False] * 256
        for char in charList:
            if charList[ord(char)] == True:
                return False
            else:
                charList[ord(char)] = True
    return True
    