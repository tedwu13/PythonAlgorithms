# using a list to store each char and change space to '%20', then join list into a string
def replaceSpaces(string):
    charList = []
    for char in string:
        if char == ' ':
            char = '%20'
            charList.append(char)

    return ''.join(charList)

