#  def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         else:
#             print('found')


# def countdown(i):
    #base case
#     if i < 1:
#         return 
#     else:
        #recursive case
#         print(i)
#         countdown(i-1)
    
# countdown(3)


#Call stack
# def greet(name):
#     print("Hello " + name + "!")
#     greet2(name)
#     print("getting ready to say bye....")
#     bye(name)
#     print("all Done")
    
    
# def greet2(name):
#     print("How are you " + name + "?")
    
# def bye(name):
#     print("Ok bye..." + name + "!")
    
# greet("Seyi")

def factorialRec(num):
    if num <= 1:
        return num
    else:
        num =num *  factorialRec(num - 1)
        return num


print(factorialRec(4))