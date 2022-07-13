

def factors(n):
    result = []
    
    for k in range(1, n + 1):
        if n % k == 0:
            result.append(k)
    return result

#generator creation using keyword 'yield'
def factor(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k

# print(factors(3))
# print(factor(3))

def factorsNum(n):
    k = 1
    message = "Factors are"
    while k * k < n:
        if n % k == 0:
            yield message, k
            yield n // k
        k += 1
    
    if k * k == n:
        yield k
        

def finbonacciGen():
    a = 0
    b = 1
    
    while True:
        yield a
        
        #perfom swap
        future = a + b
        a = b
        b = future
        
        #or simpler swap
        # a,b = b, a+b

# for facto in factor(24):
    # print(facto)
    
# print(finbonacciGen())

n = 5
square = [k*k for k in range(1, n + 1) ]

factos = [k for k in range(1, n + 1) if n % k == 0]

a = 10
b = 2
current = 1
n = 1

next = (a * current + b) % n

#is even
def isEven(k):
    if k % 2 == 0:
        return True
    else:
        return False
    
#min max values in an array
def minmax(data):
    #declare two variables current_min and current_max to have the first value of the array 
    current_min, current_max = data[0] , data[0]
    #loop over the array using range and the length of the array
    for d in range(1, len(data)):
        #check to see if present loop is greater than current_max value
        if data[d] > current_max:
            #if greater, let current_max hold the value of the present loop value
            current_max = data[d]
            #else if the present loop is lesser than current_min
        elif data[d] < current_min:
            #let current_min hold the value of the present loop
            current_min = data[d]
        else:
            print("Equals")
    return current_max , current_min
       
            
arr = [8,3,2,4,5,0] 
arr2 = [4, 1,5,7,]    


# print(minmax(arr))

# print(factos)
# print(square)
# print(finbonacciGen)
# print(isEven(2))

#sum of all the squares of all positive Integer
#lesser than the given Num
def findSquareSum(n):
    #declare a variable sum with an intial value of 0
    sum = 0
    #loop through the given number using range() function
    for i in range(n):
        #multiply each value at each loop and save to a variable
        square = i * i
        sum += square
        print("Square of {0} is {1}".format(i, square))
    print("Total sum of all Squares is:",sum)
        # k = i*i
        # sum =+ k
        # return sum
    
# print(findSquareSum(1000))
for i in range(50, 90, 10):
    print(i)
