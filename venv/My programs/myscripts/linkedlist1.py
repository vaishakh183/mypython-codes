#Append new nodes at the end

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=node()

    def append(self,data):
        newnode=node(data)
        cur=self.head
        while cur.next != None:  #loop startd from head
            cur=cur.next
        cur.next=newnode  #once we know we are at the last node ,add hte new node.

    def length(self):
        count=0
        cur=self.head
        while cur.next != None:
            count +=1
            cur=cur.next
        return count

    def display(self):
        elements=[]
        cur=self.head
        while cur.next != None:
            cur=cur.next
            elements.append(cur.data)
        print(elements)

    def search(self,data):
        cur=self.head
        index=0
        while cur.next != None:
            cur=cur.next
            index +=1
            if int(cur.data) == int(data):
                return index

    def get(self,index):
        if int(self.length()) < int(index):
            print("Out of range")
        else:
            cur=self.head
            cur_index=0
            while True:
                cur=cur.next
                cur_index +=1
                if int(cur_index) == int(index):
                    return cur.data

    def erase(self,index):
        cur_node=self.head
        last_node=cur_node
        count=0
        while count <=int(index):
            cur_node =cur_node.next
            count +=1
            if count == index:
                last_node.next=cur_node.next


l1=linkedlist()
l1.append(1)
l1.append(3)
l1.append(10)
l1.append(30)
l1.append(32)
l1.display()
print(l1.length())
print(l1.search(3))
print(l1.get(4))
print(l1.erase(2))
l1.display()