word = 'human'
word_lst = []
for letters in word:
    # print(letters )
    word_lst.append(letters)
# print("first normal loop",word_lst)

h_letters = [letter for letter in 'seyi']
# print("list comprehension", h_letters)

#using lambda vs list comprehension
letters = tuple(map(lambda x:x,'seyi'))
# print(letters)

#conditionals in list comprehension
number_lst = [x for x in range(20) if x % 2 == 0]
# print("Conditional list comprehension", number_lst)

#nested if with list comprehension
num_lst = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
#here list comprehension checks:
# 1- is y divisible by 2 or not
# 2- is y divisble by 5 or not
# 3 - if y satisfies both conditions, y is appended to num_lst
print("Nested if in list comprehension:", num_lst)

#if...else with list comprehension
obj = ["Even" if i % 2 ==0 else "Odd" for i in range(10)]
print(obj)

#nested loops in list comprehension
"""Suppose, we need to compute the transpose of a matrix that requires nested 
for loop. 
Let’s see how it is done using normal for loop first."""

"""Using normal for loop"""
transposed = []
matrix = [
            [1,2,3,4],
            [4,5,6,8]
        ]


matrix2 = [
            ['seyi','funmi','gbemi'],
            ['Ase','Ini','Anjola', 'Ara',]
        ]

for i in range(len(matrix2[0])):
    transposed_row = []
    
    for row in matrix2:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    
print("transposed matrix using for loop", transposed)

"""using list comprehension"""
matrixs = [
            [1,2], 
            [3,4], 
            [5,6],
            [7,8]
        ]
transpose = [[row[i] for row in matrix2] for i in range(3)]
print(f"list comp: {transpose},'\n'")

