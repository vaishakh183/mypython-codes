#Very first node is called root node. there is a root pointer to data part of it.
#node has two parts ,data part and next pointer part, next pointer part is pointing to data part of next node.
#Sameway last node in the list does not have a next pointer because there is no next node.

#example add new node(10) at first. first we create a new node, we put 10 in data block, then we point the next block to root node. then we change to root node
#to 10 data block.

#to remove, first we have to find the value(eg:5),so we start from first node and compare data . when we find 5. first change next pointer of its pervious node
#to 5's next node. thats it. basically 5 node is still there but it is excluded from linked list.
#The first node is called the head. If the linked list is empty, then the value of the head is NULL.
#user cannot access head node. It is just a implimentation for identifying the first node.

class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def getdata(self):
        return self.data
    def setdata(self,data):
        self.data=data
    def getnext(self):
        return self.next
    def setnext(self,next):
        self.next=next

class linkedlist():
    def __init__(self,root=None):
        self.root=root
        self.size=0

    def getsize(self):
        return  self.size

    def add(self,data):
        newnode=node(data,self.root)
        self.root=newnode
        self.size +=1

mylist=linkedlist()
mylist.add(3)
mylist.add(5)
mylist.add(1)
print(mylist.getsize())

print(mylist)

