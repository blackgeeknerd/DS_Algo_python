def removeDuplicate(arr, b, counter=0):
    """Program that removes duplicate element from an array and return the cleaned version
    
    arr     is the array,
    b       is the length of the array,
    counter is the counter with default value 0
    """
    new = []
    last = []
    while counter < b:
        if arr[counter] == arr[counter - 1]:
            new.append(a[counter])
        else:
            last.append(a[counter])
        counter = counter + 1
    print("old array with duplicates", arr)
    return "Cleaned Array no duplicate" , last


a = [1,2,3,4,1,2,6,8,9,6,7,1,4,1,2,3,4,5,6,5]
# a = [1,4,1,2,3,4,5,6,5]
a.sort()
c = len(a)
d = 0
print(removeDuplicate(a, c, d))