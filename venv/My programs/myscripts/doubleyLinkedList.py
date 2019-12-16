class node:
    def __init__(self,data=None):
        self.data=data
        self.next_node=None
        self.prev_node=None

class doublelinedlist:
    def __init__(self):
        self.head=node()


    def addfirst(self,data):
        cur_node=node(data)
        cur_node.next_node=self.head
        self.head.prev_node=cur_node
        self.head=cur_node

    def addlast(self,data):
        newnode=node(data)
        cur_node=self.head
        while cur_node.next_node !=None:
            cur_node=cur_node.next_node
        cur_node.next_node=newnode
        newnode.prev_node=cur_node
        newnode.next_node=None



    def display(self):
        cur_node=self.head
        l1=[]
        while cur_node.next_node !=None:
            l1.append(cur_node.data)
            cur_node=cur_node.next_node
        print(l1)

a=doublelinedlist()
#a.addfirst(10)
#a.addfirst(20)
a.addfirst(30)
a.addfirst(40)
a.addlast(50)
a.display()