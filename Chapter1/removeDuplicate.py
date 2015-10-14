def removeDuplicate(arr):
# use a dictionary to store all characters 
# and then check dictionary if there is duplicate
# if duplicate, don't add to output
# else add to output

dupDictionary = {}
output = []

for i in range(len(arr)):
    element = arr[i]
    if not dupDictionary[element]:
        output.add[element]
        dupDictionary[element] = True
return output

