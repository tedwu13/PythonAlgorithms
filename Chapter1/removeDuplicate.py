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
        output.append(element)    
        dupDictionary[element] = True
return output

# [1,1,2,3,4,5]
# output = [1,2,3,4,5]
def removeDup(arr):
    dupDictionary = {}
    output = [] 
    for i in range(len(arr)):
        element = arr[i]
        if not dupDictionary[element]:
            dupDictionary[element] = True
            output.append(element)
    return output
