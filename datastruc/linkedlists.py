
# 1 - start with a single node
class Node:
    #constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
#creating a single node
# first = Node(3)
# print(first.data)

# 2 - Join nodes to get a linked list
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    #insert method for the linkedlist
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            
    #print method for the linked list
    def printLL(self):
        current = self.head
        while(current):  
            print(current.data)
            current = current.next
            
                    
#linked list with a single node
LL = LinkedList()
LL.insert(3)
LL.insert(5)
LL.insert(4)

LL.printLL()