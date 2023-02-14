import random


from tree import Tree
from tree import print_tree, print_visual, read_tree_from_file

from node import Node


test_count = 20
nodes = []
for i in range(test_count):
    nodes.append(Node(i, 'title', 'description'))

tree = Tree("tree1", nodes[0])

for i in range(1, test_count):
    index = random.randint(0, i-1)
    tree.insert(nodes[index], nodes[i])

print("*" * 30)
print("before")
print_visual(tree.root, 0)

tree.write_tree_in_file()

tree = read_tree_from_file("tree1")

print("*" * 30)
print("after")
print_visual(tree.root, 0)




