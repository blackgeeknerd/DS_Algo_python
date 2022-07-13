from array import array
from itertools import permutations


primes = array('f', [2.01])
primer = list(primes)
# print(primer)

# print(primes)

#displaying the 
import sys

data = []
n = 10
sum = 0
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    
    # print('Length: {0:3d}; ; Size in bytes: {1:4d}'.format(a, b))
    sum+=b
    data.append(None)
# print('Total byte used is: {0}'.format(sum))

def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    
    yield weekdays[index]
    yield weekdays[index + 1]
    
day = testgen(4)
# print( next(day), next(day))

#convert list to string
weekdays = ['sun','mon','tue','wed','thu','fri','sat']

listToString = ' '.join(weekdays)
# print("This is changing a list to a string", listToString)
message = "Hello my love"
splitMessage = message.split()
# print('This is first split {0}'.format(splitMessage))
# print(splitMessage[0])
# print(split(message))
messageToList = list(message)
# print('This is converting str to list {0}'.format(messageToList))
# messageToList.split()
# print(messageToList)

#count the occurance of an element in a list
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
weekcount = [1, 2, 3, 1, 2,3,5,6]
weekresult = weekcount.count(1)
print(weekresult)

dayCount = weekdays.count('mon')
# print(dayCount)

# print([[x, weekdays.count(x)] for x in set(weekdays)])
# print([[x , weekdays.count(x)] for x in weekdays])

# print(weekdays[-1])

names = ['Chris', 'Jack', 'John', 'Daman']

# print(names[-1][-1])
# print(names[-1][-2])

#Enumerate function
subjects = ["Python", "Interview", "Questions"]
# for i, subjects in enumerate(subjects):
#     print(i, subjects)

#sorting a list
lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']

#using sort()
lst.sort()
# print(lst)

#using sorted()
sortedlst = []
# for ele in sorted(lst):
    # sortedlst.append(ele)
# print(sortedlst)
    # print(ele)
    
#sorting by length of strings
lst = ['Geeksforgeeks', 'is', 'a', 'portal', 'for', 'geeks']

#using the sort() with key as len
lst.sort(key = len)
# print(lst)

#sorting string by integer value
lst =  ['23', '33', '11', '7', '55']

#using sort() with key as int
lst.sort(key = int)
# print(lst)

#sorting in descending order
lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']

#using sort() 
lst.sort(reverse=True)
# print(lst)

fst = [9, 2, 1, 6, 4, 5, 7, 8, 3]
sorted_fst = sorted(fst)
# print(sorted_fst)
# fst.sort()
# print(fst)
# print(fst.sort()) #returns None


"""Sorting list with mixed datatype"""

#method 1
def mix(num):
    try:
        ele = int(num)
        return (0, ele, '')
    except ValueError:
        return (1, num, '')

#initialize list
test_list = [4, 'gfg', 2, 'best', 'is', 3]
test_list.sort(key = mix)

# print(test_list)

# print(sorted([str(x) for x in test_list]))



chk_str = 'ball'
Alist = ['fly','on', 'o', 'hot', 'ball', 'air']

# def findstring(strchk, biglist):
#    for i in range(2, len(biglist) + 1):
#       for perm in permutations(biglist, i):
#          if ''.join(perm) == strchk:
#             return True
#    return False

# # Using the function
# if(findstring(chk_str,Alist)):
#    print("String can be formed.")
# else:
#    print("String can not be formed.")

"""Sort the characters of a string"""
str1 ='apple'
sorted_chars = sorted(str1)
sorted_string = ''.join(sorted_chars)
print(sorted_chars)
print(sorted_string)   

        
    
"""Method 2"""
