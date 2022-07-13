from functools import lru_cache


class LinkedList:
    
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
        
    # @lru_cache(maxsize=16)
    def visualize(self):
        node = self.head
        nodes = []
        # string_repr =""
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes) 
    
    
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
    def add_last(self, node):
        #if head is empty , set node as head
        if self.head is None:
            self.head = node
            return
        #else loop through the linked list 
        # and set the last node as value of node
        for current_node in self:
            pass
        current_node.next = node
        
    def add_after(self, target_node_data, new_node):
        
        if self.head is not None:
            raise Exception("List is Empty!")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
            
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is Empty")
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
            
        raise Exception("Node with data '%s' not found" % target_node_data)
        

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
        
        
first_node = Node(str(10))
second_node = Node(str(11))
third_node = Node(str(5))

l_list = LinkedList()

l_list.head = first_node
first_node.next = second_node
second_node.next = third_node

# node = l_list.head

print(l_list.visualize())
for node in l_list:
    print(node)

# print(first_node.next)
l_list.add_first(Node('8'))
print(l_list.visualize())
l_list.add_last(Node('9'))
print(l_list.visualize())
l_list.add_before('5', Node('1'))
print(l_list.visualize())




