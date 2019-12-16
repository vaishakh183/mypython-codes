class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=node()

    def addfirst(self,data):
        newnode=node(data)
        curnode=self.head
        newnode.next=curnode
        self.head=newnode

    def addend(self,data):
        newnode=node(data)
        print(newnode.data)
        curnode=self.head
        print(curnode.data)
        while curnode.next !=None:
            curnode=curnode.next
        curnode.next=newnode
        head=self.head
        newnode.next=head

    def check_circle(self):
        first=self.head
        second=self.head
        while second.next !=None:
            if first == second:
                return True
            second=second.next



    def display(self):
        curnode=self.head
        l1=[]
        while curnode !=None:
            l1.append(curnode.data)
            curnode=curnode.next
        print(l1)



a=linkedlist()
a.addfirst(1)
a.addfirst(2)
a.addfirst(3)
a.addfirst(4)
a.addfirst(5)
#a.addend(6)
a.display()
print(a.check_circle())