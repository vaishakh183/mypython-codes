#Append new nodes at first

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

#When the list is first initialized it has no nodes, so the head is set to None. (Note: the linked list doesn’t necessarily require a node to initialize.
class linkedlist:
    def __init__(self):
        self.head=Node()
# the simplest way to do it is to place node at the head of the list and point the new node at the old head (sort of pushing the other nodes down the line).
    def insert(self,data):
        new_node=Node(data)
        cur_node=self.head
        new_node.next=cur_node
        self.head=new_node
        print(new_node.data)

    def length(self):
        cur=self.head
        count=0
        while cur.next != None:
            cur=cur.next
            count +=1
        print(count)

    def display(self):
        cur=self.head
        l1=[]
        while cur.next !=None:
            l1.append(cur.data)
            cur=cur.next
        print(l1)



a=linkedlist()
a.insert(5)
a.insert(6)
a.insert(6)
a.length()
a.display()