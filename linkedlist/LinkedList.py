class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self,data):
        self.data = data
        self.head = None
        self.next = None
    def push(self,data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def print(self):
        node = self.head
        while node!=None:
            print(node.data)
            node = node.next
