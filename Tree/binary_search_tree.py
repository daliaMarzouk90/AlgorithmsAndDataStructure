from Node import Node

class Binary_Search_Tree:
    def __init__(self, compaire_function = None):
        self.root = Node(None)
        if(compaire_function == None):
            self.compaire_function = lambda a,b: a > b
        else:
            self.compaire_function = compaire_function

    def insert(self, data):
        if(self.root.data == None):
            self.root.data = data
            return
        
        new_node = Node(data)
        if(self.compaire_function(self.root.data, data)):
            if(self.root.l_child == None):
                self.root.l_child = new_node
                return

            ptr = self.root.l_child
        else:
            if(self.root.r_child == None):
                self.root.r_child = new_node
                return

            ptr = self.root.r_child
        while(ptr != None):
            if(self.compaire_function(ptr.data, data)):
                if(ptr.l_child == None):
                    ptr.l_child = new_node
                    return

                ptr = ptr.l_child
            else:
                if(ptr.r_child == None):
                    ptr.r_child = new_node
                    return

                ptr = ptr.r_child

    def find(self, value, compair_function = None):
        if(compair_function == None):
            compair_function = lambda a: 1 if a > value else ( -1 if a < value  else 0)

        if(self.root.data == None):
            return None

        ptr = self.root
        while ptr != None:
            comparison_value = compair_function(ptr.data)
            if comparison_value == 0:
                return ptr
            elif comparison_value == 1:
                ptr = ptr.r_child
            else:
                ptr = ptr.l_child

        return None