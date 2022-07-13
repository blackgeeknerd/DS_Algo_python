def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    
    The search only considers the portion from data[low] to data[high] inclusive
    """
    
    if low > high:
        return False        #interval is empty no match found
    else:
        mid = (low + high) // 2
        
        if target == data[mid]: #match found
            return True, data[mid]
        elif target < data[mid]:
            #recur on the portion to the left
            return binary_search(data, target, low, mid - 1)
        else:
            #recur on the portion to the right
            return binary_search(data, target, mid + 1, high)
        
        
     

datalist = [8,3,4,2,7,9,5,7]
targetnum = 3   

print(binary_search(datalist,targetnum,1,9))