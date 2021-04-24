class static_stack:
    def __init__(self, size):
        self.size = size
        self.container = [0] * size
        self.peek = 0

    def push(self, data):
        if(self.peek == self.size):
            print("stack is full")
            return

        self.container[self.peek] = data
        self.peek = self.peek + 1

    def pop(self):
        if(self.peek == 0):
            print("stack is empty")
            return

        self.peek = self.peek - 1
        return self.container[self.peek]

class dynamic_stack:
    def __ini__(self, init_size, increment_size):
        self.size = init_size
        self.increment_size = increment_size
        self.container = [0] * init_size
        self.peek = 0

    def push(self, data):
        if(self.peek == self.size):
            extension_list = [0] * self.increment_size
            self.container = self.container + extension_list

        self.container[self.peek] = data
        self.peek = self.peek + 1

    def pop(self):
        if(self.peek == 0):
            print("stack is empty")
            return

        self.peek = self.peek - 1
        return self.container[self.peek]