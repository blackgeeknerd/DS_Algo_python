# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

#1 - Using the brute-force method
'''
    steps...
        identify the values in the array 'arr[i]',by looping thru d array using the length - 1 as range ..range(len(arr) - 1)
        loop through the length of the array using the index counter 'i' as start point: for j in range(i + 1, len(arr)):
    check to see if the sum of the value of arr[i] + arr[j] equals the target using if
    if they match the target, print them out
'''

def findSum(arr, target):
    
    #consider each elements except the last
    for i in range(len(arr) - 1): #length of arr - 1 = 5(number of index)
        # print('iteration of i:', arr[i])
        #start from the i element until the last element
        for j in range(i + 1, len(arr)): #start range from i + 1, stop at lenght of arr 
            if arr[i] + arr[j] is target:
                print("Pair found ", arr[i] , arr[j])
    return
        
        
#2 - using the sorting method
'''
    -first we sort the array in ascending order using the sort()
    -create/maintain two variables/points/indices pointing to the list/array endpoints, which are the 0 index and the last index
    - we now check against each array loop value using the two points as array[index] to access the value example:
        arr[low] + arr[high] == target 
            which translates to arr[0] + arr[8] on the first loop
                                arr[1] + arr[8] or  arr[0] + arr[7]  on the second loop 
'''

def targetSumSort(arr, target):
    
    #sort the array in ascending order
    arr.sort()
    
    #create/maintain two variables/points/indices pointing to the list/array endpoints, which are the 0 index and the last index
    (low, high) = (0, len(arr)-1)
         
    while low < high:
        
        #check if value of low with high equals the target, if it does, print it out
        if arr[low] + arr[high] is target:
            print("Pair found", (arr[low], arr[high]))
        
        
        if arr[low] + arr[high] < target:
            low = low + 1
        else:
            high = high - 1
    print("Pair not found")
    
    
#using the Hash method
def findPair(arr, target):
    
    #create an emppty dictionary
    d = {}
    
    #do for each element
    print("Key\tValue")
    for key, value in enumerate(arr):
            # print(key,'\t',value)
        if target - value in d:
            
            print("pair found '{0} + {1}= {2}'".format(target-value, value, target))
        d[value] = key 
        # print(key, value)
    return
    
    print("pair not found")

arrayNum = [8, 7, 2, 5, 3, 1,5,6,4]
arrayNum2 = []
for i in arrayNum:
    new = i / 2
    arrayNum2.append(new)
print(arrayNum2)
    
target = 5
# print(len(arrayNum))
findSum(arrayNum, target)

# targetSumSort(arrayNum, target)

# findPair(arrayNum2, target)