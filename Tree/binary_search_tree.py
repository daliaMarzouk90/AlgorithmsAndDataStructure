class Node:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None

    def in_order_traverse(self, nodes_array = []):
        if(self.data == None):
            return nodes_array

        if(self.l_child != None):
            nodes_array = self.l_child.in_order_traverse(nodes_array)

        nodes_array.append(self.data)

        if(self.r_child != None):
            nodes_array = self.r_child.in_order_traverse(nodes_array)

        return nodes_array

    def pre_order_traverse(self, nodes_array = []):
        if(self.data == None):
            return nodes_array

        nodes_array.append(self.data)

        if(self.l_child != None):
            nodes_array = self.l_child.pre_order_traverse(nodes_array)

        if(self.r_child != None):
            nodes_array = self.r_child.pre_order_traverse(nodes_array)

        return nodes_array

    def post_order_traverse(self, nodes_array = []):
        if(self.data == None):
            return nodes_array

        if(self.l_child != None):
            nodes_array = self.l_child.post_order_traverse(nodes_array)

        if(self.r_child != None):
            nodes_array = self.r_child.post_order_traverse(nodes_array)

        nodes_array.append(self.data)

        return nodes_array


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

comparison_function = lambda a,b: a["value"] > b["value"]
tree = Binary_Search_Tree(compaire_function = comparison_function)

nodes_data = [{"key": "A", "value": 30}, 
              {"key": "B", "value": 10},
              {"key": "C", "value": 2},
              {"key": "D", "value": -7},
              {"key": "E", "value": 4},
              {"key": "F", "value": 100},
              {"key": "J", "value": 66},
              ]

for i in range(len(nodes_data)):
    tree.insert(nodes_data[i])

nodes_array = tree.root.post_order_traverse()
print("***post_order***")
for i in range(len(nodes_array)):
    print(nodes_array[i]["key"])

print("***pre_order***")
nodes_array = tree.root.pre_order_traverse()
for i in range(len(nodes_array)):
    print(nodes_array[i]["key"])

print("***in_order***")
nodes_array = tree.root.in_order_traverse()
for i in range(len(nodes_array)):
    print(nodes_array[i]["key"])