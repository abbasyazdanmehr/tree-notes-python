import os

from controllers import controller_menu, controller_main
import paths
from models.tree import Tree
from models.node import Node
from models.tree import print_visual, read_tree_from_file
from views.view_menu import print_menu
from constants import REPRESENT_APP_NAME

def new_node(keys):
    print()
    print("$ Node: ")

    while True:
        print('- key(must be number): ', end='')
        in_key = int(input())

        if in_key == -1:
            return

        if not (in_key in keys):
            break
        else:
            print("key exists")

    print('- title: ', end='')
    in_title = input()

    print('- content: ', end='')
    in_content = input()

    return Node(in_key, in_title, in_content)


def edit_node():
    print()
    print("$ Node: ")

    print('- title: ', end='')
    in_title = input()

    print('- content: ', end='')
    in_content = input()

    return Node(-1, in_title, in_content)


def view_tree(tree_name):
    command = 0
    tree = read_tree_from_file(tree_name)
    while True:
        while True:
            print()
            print('$ Edit Tree: ')
            print(tree_name)
            print_visual(tree.root, 0)

            print()
            print('1. new node')
            print('2. edit node')
            print('3. delete node (cascade)')
            print('4. save')
            print('-1 for back')
            print()
            print('- Choose by number: ', end='')
            command = input()

            if command == '1':
                my_new_node = new_node(tree.get_all_keys())

                print()
                print('- input parent key: ', end='')
                parent_key = int(input())

                if (tree.insert_by_parent_key(parent_key, my_new_node)):
                    print("success!")

            elif command == '2':
                print("Input node key: ", end='')
                my_node_key = int(input())
                my_node = tree.get_node_by_key(my_node_key)
                
                if my_node == None:
                    print()
                    print("key not found!")
                else:
                    temp_node = edit_node()
                    my_node.title = temp_node.title
                    my_node.content = temp_node.content
                    print("success!")

            elif command == '3':
                
                print("Input node key: ", end='')
                my_node_key = int(input())
                my_node = tree.get_node_by_key(my_node_key)
                
                if my_node == None:
                    print()
                    print("key not found!")
                else:
                    print("Are you shure to delete? (yes) ", end='')
                    verif = input()
                    if verif == "yes":
                        tree.cascade_delete(tree.root, my_node)
                        print("success!")
            elif command == "4":
                tree.write_tree_in_file()
                
            elif command == "-1":
                break

        if command == "-1":
            print()
            print("Save? (yes) ", end='')
            inp = input()

            if inp == "yes":
                tree.write_tree_in_file()
                print('success!')

            break


def print_all_trees_name():
    files_name = os.listdir(paths.trees_path)
    for j in files_name:
        if ".txt" in j:
            print(" - " + j[:-4])


def view_all_trees():

    while True:
        print()
        print("$ Trees: ")
        files_name = os.listdir(paths.trees_path)
        print_all_trees_name()

        while True:

            print()
            print("- Type Tree name to edit: (-1 for back) ", end='')
            command = input()

            if command == '-1':
                break

            command += ".txt"
            if command in files_name:
                view_tree(command[:-4])
                break
            else:
                print('no tree with this name!')

        if command == '-1':
            break


def new_tree():
    print()
    print("$ Create new Tree:")

    while True:
        print(" - tree name: ", end='')
        tree_name = input()

        if not ((tree_name + ".txt") in os.listdir(paths.trees_path)):
            break
        else:
            print("tree name already exists!")
            print()

    sample_root = Node(0, 'sample subject', 'sample content')
    sample_tree = Tree(tree_name, sample_root)

    print()
    print("Are you shure to create? (yes) ", end='')
    command = input()
    if command == 'yes':
        sample_tree.write_tree_in_file()


def main_loop():
    while True:
        print_menu(REPRESENT_APP_NAME, ['view all trees', 'new tree'])
        print("- Choose by number: ", end='')

        command = input()

        print()

        if command == '1':
            view_all_trees()
        elif command == '2':
            new_tree()
        elif command == '3':
            exit()


main_loop()
