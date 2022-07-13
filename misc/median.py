def findMedian(a, n):
    """Program that finds the median value of a list/array
    
    
    a    a is the array value
    n    n is the length of the array
    """
    
    #first sort the array
    sorted(a)
    print(a[int(n - 1)])
    print(a[int(n)])
    #check for even case
    if n % 2 != 0:
        return float(a[n // 2] )
    
    return float((a[int((n - 1)/2)] + 
                  a[int(n / 2)]) / 2.0)
    
    
a = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
n = len(a)

print("median = " , findMedian(a, n))