def findSmallest(arr):
    
    firstIndexValue = arr[0]
    firstIndex = 0
    
    for i in range(1, len(arr)):
        if arr[i] < firstIndexValue:
            firstIndexValue = arr[i]
            firstIndex = i
    return firstIndex


def sortList(arr):
    new_list = []
    
    for i in range(0, len(arr)):
        smallest = findSmallest(arr)
        new_list.append(arr.pop(smallest)) 
    return new_list
    
word = [2,3,6,7,8,10,1,11,5,]
print(sortList(word))