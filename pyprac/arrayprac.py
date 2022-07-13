message = ['hell', 'ho', 'tel', 'let', 'lol', 'hi', 'hu', 'sad' , 'tell', 'holy', 'oooh', 'boy' , ]
# test = "huhyisdftelol"
test = 'byuaiboylet'
# test = "huhyisdftelolkhsadgiyeqiuohobiugfkiuyi"


# test = 'khsadgiyeqiu'
test_lst = [*test]
# print(test_lst)
# print("i\ti-1\ti+1")
count = 0
new_lst =[]
for i in range(len(test)-1,-1,-1):
    for j in range(len(new_lst)):
        # if test[i] + new_lst[j]  in message:
        new_lst.append(test[i] + new_lst[j] )
    new_lst.append(test[i])
        # if test_lst[i]+ test_lst[j] + test[j] + test[j] in message:
        #     new_lst.append(test_lst[i] + test_lst[j] + test[j] + test[j])
        # if  test_lst[i] + test_lst[j] + test[j] + test[i] in message:
        #     new_lst.append(test_lst[i] + test_lst[j] + test[j] + test[i])
        # if test_lst[i-1] + test_lst[i] + test_lst[i] in message:
        #     new_lst.append(test_lst[i-1] + test_lst[i]+test_lst[i])
        # if test_lst[i] + test_lst[j]  in message:
        #     new_lst.append(test_lst[i] + test_lst[j])
        
test_str = []
 
for ele in new_lst:
    if ele in message:
        test_str.append(ele)
    test_str = set(test_str)
    test_str = list(test_str)       
print(test_str)
    


    
