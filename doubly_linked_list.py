class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, previous):
        self.previous = previous

    def get_prev(self):
        return self.previous

class Double_Linked_List:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        
        if(self.head != None):
            self.head.previous = new_node

        self.head = new_node

        if(self.tail == None):
            self.tail = new_node

    def size(self):
        """
        get linked list size
        """
        size = 0
        node = self.head
        while node != None:
            node = node.next
            size = size + 1
        
        return size

    def deletion(self):
        """
        delete from the begining
        """
        if(self.head == None):
            return
        if(self.head.next != None):
            self.head.next.previous = None
            self.head = self.head.next
        else:
            self.head = None

    def insert_last(self, data):
        new_node = Node(data)
        if(self.tail != None):
            self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

        if(self.head == None):
            self.head = new_node

    def deletion_last(self):
        if(self.tail == None):
            return

        if(self.tail.previous):
            self.tail = self.tail.previous

        self.tail.next = None
        


