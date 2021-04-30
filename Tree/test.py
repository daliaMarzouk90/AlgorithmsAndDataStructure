#%%
from binary_search_tree import Binary_Search_Tree

#%%
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
#%%
comparison_function = lambda a,b: a["value"] > b["value"]
nodes_data = [{"key": "A", "value": 30}, 
              {"key": "B", "value": 10},
              {"key": "C", "value": 2}]
tree = Binary_Search_Tree(compaire_function = comparison_function)

for i in range(len(nodes_data)):
    tree.insert(nodes_data[i])

tree.root = tree.root.right_rotation()
print("---in_order---")
nodes_array = tree.root.in_order_traverse()
for i in range(len(nodes_array)):
    print(nodes_array[i]["key"])
#%%
comparison_function = lambda a,b: a["value"] > b["value"]
nodes_data = [{"key": "C", "value": 2},
              {"key": "B", "value": 10},
              {"key": "A", "value": 30}]
tree = Binary_Search_Tree(compaire_function = comparison_function)
for i in range(len(nodes_data)):
    tree.insert(nodes_data[i])
tree.root = tree.root.left_rotation()
nodes_array = tree.root.in_order_traverse()
print("---in_order---")
for i in range(len(nodes_array)):
    print(nodes_array[i]["key"])

# %%

