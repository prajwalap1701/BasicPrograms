class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, prev_data):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == prev_data:
                prev_node = n
                break
            n = n.ref
        if prev_node.ref == None:
            prev_node.ref = new_node
        else:
            temp = prev_node.ref
            prev_node.ref = new_node
            new_node.ref = temp

    def add_before(self, data, pre_data):
        new_node = Node(data)
        n = self.head
        if n.data == pre_data:
            temp = self.head
            self.head = new_node
            new_node.ref = temp
            return

        while n is not None:
            if n.data == pre_data:
                break
            prev_node = n
            n = n.ref

        temp = prev_node.ref
        prev_node.ref = new_node
        new_node.ref = temp


ll = LinkedList()
ll.add_begin(50)
ll.add_begin(20)
ll.add_begin(30)
ll.add_begin(70)

ll.add_end(100)
ll.add_end(120)
ll.add_begin(60)

ll.add_after(200, 50)
ll.add_before(300, 60)



print(ll.print_LL())