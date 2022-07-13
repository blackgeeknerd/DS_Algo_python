word = "pynative"
word_char = [*word]
n = 4

def removechar(word, number):
    """Program to remove n number of character in a string"""
    
    newlst = []
    convertword = [*word]
    for i in range(0, len(word)):
        if i >= number:
            newlst.append(convertword[i])
    # print(newlst)
    wunmi = ''.join(newlst)
    return wunmi


# print(removechar(word, 1))

#my solution
def multiplication_table(size):
    """Create a multiplication table"""
    print("Multiplication table")
    for i in range(1,size+1):
    
        print("{} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>3} {:>3} {:>3}".format(i, (i+i), (i+i*2), (i+i*3), (i+i*4), (i+i*5),(i+i*6), (i+i*7),(i+i*8),(i+i*9)))
      
print(multiplication_table(12))


#article solution
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")
    
    
"""Downward asterix"""
#my solution/algorithm
# for i in range((6)-1,-1,-1):
    # print('*'* i)
    
#article solution
# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

def exponen(base, exp):
    c = base ** exp
    return c

# print(exponen(5,4))