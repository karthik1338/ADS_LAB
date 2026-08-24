class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self,data):
        node = Node(data,self.head)
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_end(self,data):
        node = Node(data)
        if not self.head:
            self.tail = self.head = node
            return
        self.tail.next = node
        self.tail = node

    def insert_position(self,data,pos = 0):
        if pos<= 0 or not self.head:
            self.insert_begin(data)
            return 
 

        count = 1
        curr = self.head
        while curr.next and count != pos:
            curr = curr.next
            count+= 1
        if curr.next:
            node = Node(data)
            node.next = curr.next
            curr.next = node
        else:
            print("Position not found, element is added at the end")
            self.insert_end(data)
    
    def delete_by_value(self,val):
        if not self.head:
            print("Linked List is empty")
            return 
        elif self.head.data == val:
            if self.head == self.tail: self.tail = None
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != val:
            curr = curr.next
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
        else:
            print("Value not found")

    def search(self,val):
        curr = self.head
        count = 0
        while curr:
            if curr.data == val:
                print("Element found in pos",count)
                break
            curr = curr.next
            count+=1
        else:
            print("Value not found")

    def head_tail(self):
        if not self.head:
            print(f'head --> NULL\ntail --> NULL')
            return
        print('head -->',self.head.data)
        print("tail -->",self.tail.data) 

    def traverse(self):
        current = self.head
        if not current : 
            print("Linked List is empty.") 
            return
        while current :
            print(f"{current.data} -->",end = " ")
            current = current.next
        print("NULL")

        self.head_tail()


if __name__ == "__main__":
    ll = LinkedList()
    # Sample linked list
    n = int(input("Enter length of the Linked list"))
    for i in range(n):
        val = int(input("Enter the Elements : "))
        ll.insert_end(val)
    print("\nTraversal of linked list\n")
    ll.traverse()
    print("\nInsertion at the begining\n")
    val = int(input('Enter the val '))
    ll.insert_begin(val)
    ll.traverse()
    print("\nInsertion at the end\n")
    val = int(input('Enter the val '))
    ll.insert_end(val)
    ll.traverse()
    print("\nInsertion at a position\n")
    val = int(input('Enter the val '))
    pos = int(input("Enter the pos "))
    ll.insert_position(val,pos)
    ll.traverse()
    print("\nDelection by value \n")
    val = int(input('Enter the val '))
    ll.delete_by_value(val)
    ll.traverse()
    print("\nSearching the index of value\n")
    val = int(input('Enter the val '))
    ll.search(val)
    ll.traverse()



