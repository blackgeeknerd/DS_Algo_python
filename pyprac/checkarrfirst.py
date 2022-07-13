 
   
message = ["hell", "ho", "tel", 'lol', 'hi', 'hu', 'baby', 'sad' , 'tell', 'holy', 'oooh', 'dug', 'let', 'bug']
test = "huhyisdftelolkhsadgiyeqiuohobiugfkiuyi"

# test = 'khsadgiyeqiuohobiugfkiuyi'
# test = 'byuaiboylet'

#converting string to a list with indivical character/letter as an index
# test_lst = list(test) 
# word_test = [*test]
# list_test = []

def checkforstring(word, arr):
    
    list_test = []
    final_list = []
    counter = 0
  
    for char in range(len(word)-1,-1,-1):
        # print(word[char] + word[char - 1])
        for text in range(len(list_test)): 
            list_test.append(word[char] + list_test[text]) 
            counter = counter+1
        list_test.append(word[char])
    print("Length",len(list_test))
    print("Counter",counter)
    return  len(list_test) - counter
        
            
            
    #         list_test.append(word[char] + list_test[text])  
    #     list_test.append(word[char])
    # return list_test
    
    # for element in list_test:
    #     if element in arr:
    #         final_list.append(element)
        
    # if final_list: 
    #     final_list = set(final_list)
    #     final_list = list(final_list)
    # return final_list 
        
print(checkforstring(test, message))