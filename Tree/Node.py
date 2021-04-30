class Node:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None

    def in_order_traverse(self, _nodes_array = None):
        if(_nodes_array == None):
            _nodes_array = []

        if(self.data == None):
            return _nodes_array

        if(self.l_child != None):
            nodes_array = self.l_child.in_order_traverse(_nodes_array)

        _nodes_array.append(self.data)

        if(self.r_child != None):
            _nodes_array = self.r_child.in_order_traverse(_nodes_array)

        return _nodes_array

    def pre_order_traverse(self, _nodes_array = []):
        if(self.data == None):
            return _nodes_array

        _nodes_array.append(self.data)

        if(self.l_child != None):
            _nodes_array = self.l_child.pre_order_traverse(_nodes_array)

        if(self.r_child != None):
            _nodes_array = self.r_child.pre_order_traverse(_nodes_array)

        return _nodes_array

    def post_order_traverse(self, _nodes_array = []):
        if(self.data == None):
            return _nodes_array

        if(self.l_child != None):
            _nodes_array = self.l_child.post_order_traverse(_nodes_array)

        if(self.r_child != None):
            _nodes_array = self.r_child.post_order_traverse(_nodes_array)

        _nodes_array.append(self.data)

        return _nodes_array

    def right_rotation(self):
        if(self.l_child == None or self.l_child.l_child == None):
            return self

        r_child = self
        new_root = self.l_child
        l_child = new_root.l_child
        r_child.l_child = None

        self = new_root
        self.l_child = l_child
        self.r_child = r_child

        return self

    def left_rotation(self):
        if(self.r_child == None or self.r_child.r_child == None):
            return self

        l_child = self
        new_root = self.r_child
        r_child = self.r_child.r_child
        l_child.r_child = None 

        self = new_root
        self.l_child = l_child
        self.r_child = r_child

        return self
    
    def left_right_rotation(self):
        if(self.l_child == None or self.l_child.r_child == None):
            return self

        l_l_child = self.l_child
        l_child = self.l_child.r_child
        l_l_child.r_child = None

        self.l_child = l_child
        self.l_child.l_child = l_l_child
        
        return self.right_rotation()

    def right_left_rotation(self):
        if(self.r_child == None or self.r_child.l_child == None):
            return self

        r_child = self.r_child.l_child
        r_r_child = self.r_child
        r_r_child.l_child = None

        self.r_child = r_child
        self.r_child.r_child = r_r_child

        return self.left_rotation()

    def get_balance_factor(self, balance_factore = 0):
        if(self.l_child == None and self.r_child == None):
            return balance_factore
        
        if(self.l_child == None and self.r_child != None):
            return balance_factore + 1
        elif(self.l_child != None and self.r_child == None):
            return balance_factore + 1
        
        return get_balance_factor(balance_factore)