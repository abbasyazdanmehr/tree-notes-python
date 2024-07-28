import time
import paths

from node import Node

class Tree:
    searched = None
    all_keys = []
    sep = '`'
    def __init__(self, name, node) -> None:
        self.name = name
        self.root = node  
        self.str_file = ''
        
    def search(self, node, searching:Node): 
        if node == None:
            return None
    
        if node == searching:
            self.searched = node
            
        for i in node.children:    
            self.search(i, searching)
    
    def search_parent(self, node:Node, searching:Node): 
        if node.children == None or node.children == []:
            return None
    
        if searching in node.children:
            self.searched = node
            
        for i in node.children:    
            self.search_parent(i, searching)
    
    def search_by_key(self, node:Node, searching:int): 
        if node == None:
            return None
    
        if node.key == searching:
            self.searched = node
            
        for i in node.children:    
            self.search_by_key(i, searching)
    
    def get_node(self, node):
        self.searched = None
        self.search(self.root, node)
        return self.searched
    
    def get_parent(self, node):
        self.searched = None
        self.search_parent(self.root, node)
        return self.searched
    
    def get_node_by_key(self, key):
        self.searched = None
        self.search_by_key(self.root, key)
        return self.searched
    
    def insert(self, parent, node):
        searched_parent = self.get_node(parent)
        if searched_parent == None:
            print("not found parent")
            return False
        searched_parent.children.append(node)
        return True
        
    def insert_by_parent_key(self, parent_key, node):
        searched_parent = self.get_node_by_key(parent_key)
        if searched_parent == None:
            print("not found parent")
            return False
        searched_parent.children.append(node)
        return True
        
    def cascade_delete(self, node, searching):
        if node == None:
            return None
    
        for i in node.children:
            if i == searching:    
                node.children.remove(i)
                return None
            self.cascade_delete(i, searching)
            
    def delete(self, node, searching):
        if node == None:
            return None
    
        for i in node.children:
            if i == searching:    
                for j in searching.children:
                    node.children.append(j)
                node.children.remove(searching)
                return None
            self.delete(i, searching)
    
    def write_tree_in_file(self):
        f = open(paths.trees_path + self.name + ".txt", 'w')
        self.str_file = ''
        self.set_str_file(self.root)
        f.write(self.str_file)
        print("successfully wrote in file!")
        
    def set_str_file(self, node:Node):
        if node == None:
            return None
        
        self.str_file += str(node.key) + Tree.sep + \
            node.title + Tree.sep + node.content + Tree.sep + \
                str(len(node.children)) + Tree.sep
                
        for i in node.children:    
            self.set_str_file(i)
    
    def find_all_keys(self, node:Node): 
        self.all_keys.append(node.key)
        if node == None:
            return None
            
        for i in node.children:    
            self.find_all_keys(i)
    
    def get_all_keys(self):
        self.all_keys = []
        self.find_all_keys(self.root)
        return self.all_keys
        
    
def read_tree_from_file(tree_name:str) -> Tree:
    f = open(paths.trees_path + tree_name + ".txt", 'r')
    
    fs = f.read().split(Tree.sep)
    
    root = Node(-1)    
    make_tree(root, fs)
    
    tree = Tree(tree_name, root.children[0])

    return tree
    
    
    
def make_tree(node:Node, tree_strs:list):
    
    if tree_strs == []:
        return None
    
    key = int(tree_strs[0])
    title = tree_strs[1]
    content = tree_strs[2]
    children_count = int(tree_strs[3])
    child = Node(key, title, content)
    node.children.append(child)
    
    for _ in range(4):
        tree_strs.pop(0)
    
    for _ in range(children_count):    
        make_tree(child, tree_strs)
    
    
    

def print_tree(node:Node):
    
    if node == None:
        return None
    
    print(node)
    for i in node.children:    
        print_tree(i)
        
        
def indent(mount):
    print(('|' + ' ' * 4) * mount, end='')


def print_visual(node:Node, depth):
    if node == None:
        return None
    
    indent(depth)
    print('|')
    
    indent(depth)
    print('+---', end='')
    print(node)
    
    for i in node.children:    
        print_visual(i, depth+1)