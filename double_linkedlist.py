class Node:
    def __init__(self,prev =None,data = None,next = None):
        self.prev = prev 
        self.data = data 
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self,data):
        if not self.head:
            node = Node(None,data,None)
            self.head = self.tail = node
            return
        node = Node(None,data,self.head)
        self.head.prev = node
        self.head = node

    def insert_end(self,data):
        if not self.head:
            self.insert_begin(data)
            return
        node = Node(self.tail,data,None)
        self.tail.next = node
        self.tail = node

    def delete_begin(self):
        if not self.head:
            print("Linked List is Empty")
            return
        if not self.head.next:
            self.head = self.tail = None
            return 
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if not self.tail:
            self.delete_begin()
            return
        if not self.tail.prev:
            self.head = self.tail = None
            return 

        self.tail = self.tail.prev
        self.tail.next = None

    def delete_val(self,data):
        curr = self.traversal(data)
        if not curr:
            print("Element Not found")
            return 
        if curr == self.head:
            self.delete_begin()
            return
        if curr == self.tail:
            self.delete_end()
            return 
        curr.prev.next, curr.next.prev = curr.next, curr.prev

    def traversal(self,stop = None):
        if not self.head:
            return
        curr = self.head
        while curr:
            if curr.data == stop:
                return curr
            curr = curr.next

        return None

    def insert_after(self,target,data):
        curr = self.traversal(target)
        if not self.head:
            self.insert_begin(data)
            return
        if not curr:
            print("Target doesn't exits")
            return
        elif curr == self.tail:
            self.insert_end(data)
            return
        node = Node(curr,data,curr.next)
        curr.next.prev = curr.next = node


    def head_tail(self):
        print(f'\nhead -> {self.head.data}\ntail -> {self.tail.data}')

    def display(self):
        print('*'*100)
        if not self.head:
            print("Linked List is empty") 
            return
        curr = self.head
        print('None <->',end=' ')
        while curr:
            print(f"{curr.data} <-> ",end = '')
            curr = curr.next
        print('None')
        self.head_tail()
        print('*'*100)

d1 = DLL()
d1.insert_end(10)
d1.insert_end(20)

d1.insert_after(99, 100) 
d1.display()