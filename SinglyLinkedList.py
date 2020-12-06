class Node:

    def __init__(self, info, link=None):
        self.link = link
        self.info = info


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, info):
        newNode = Node(info)

        if self.head == None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head = newNode

    def insert_at_last(self, info):
        newNode = Node(info)

        if self.head == None:
            self.head = newNode

        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode

    def display(self):
        current = self.head
        while current.link != None:
            print(current.info)
            current = current.link
        print(current.info)

    def delete_node(self, ele):
        if self.head == None:
            print("List is Empty")
            return
        elif self.head.info == ele:
            temp = self.head
            self.head = temp.link
            temp = None
            return
        current = self.head
        while current.link != None:
            if current.link.info == ele:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link
        print("Element not found")


LL = LinkedList()
LL.insert_at_start(10)
LL.insert_at_start(5)
LL.display()
print("*********************************")
LL.insert_at_last(20)
LL.insert_at_last(30)
LL.display()
print("*********************************")
LL.delete_node(40)
LL.delete_node(20)
LL.display()
print("*********************************")
LL.delete_node(30)
LL.display()
