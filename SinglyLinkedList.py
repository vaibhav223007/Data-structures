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


LL = LinkedList()
LL.insert_at_start(10)
LL.insert_at_start(5)
LL.display()
print("*********************************")
LL.insert_at_last(20)
LL.insert_at_last(30)
LL.display()
