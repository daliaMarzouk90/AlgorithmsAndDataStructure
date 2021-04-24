class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data=None):
        """
        insert at the begining
        """
        node = Node(data)
        node.next = self.head
        self.head = node

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
        self.head = self.head.next

    def find(self, data):
        """
        find a certain item
        """
        current = self.head

        while current != None:
            if(current.data != data):
                current = current.next
                continue
            return current

        return None

    def delete(self, data):
        """
        delete a certain item
        """
        current = self.head
        previous = None

        while current != None:
            if(current.data != data):
                previous = current
                current = current.next
                continue
            break

        if current == None:
            return

        if(previous == None):
            self.head = current.next
            return

        previous.next = current.next