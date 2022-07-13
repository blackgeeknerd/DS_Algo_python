#using deque from collections to implement sometin like a linked list
#deque (double-ended queue)

from collections import deque

deck = deque()
deck = deque('abc')
deck2 = deque([{'data': 'a'}, {'data': 'b'}])
# print(deck2)
deck.append('f')
# print(deck)
deck.appendleft('d')
# print(deck)
deck.pop()
# print(deck)
deck.popleft()
# print(deck)


#a simple queue for booking restaurant orders
#implementing the Queue(FiFo)
queue = deque()

queue.append('Mary')
queue.append('John')
queue.append('Susan')

print(queue)
queue.popleft()
print(queue)


#implementing the Stack(LiFo)
#creating a simple web browser history functionality, 
# which stores every page a user visits so they can go 
# back in time easily

history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")

print(history)

history2 = deque()
history2.append("https://realpython.com/")
history2.append("https://realpython.com/pandas-read-write-files/")
history2.append("https://realpython.com/python-csv/")
print(history2)
history2.popleft()
print(history2)

