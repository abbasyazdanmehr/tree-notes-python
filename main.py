import os

import paths
from tree import Tree
from node import Node
from tree import print_visual, read_tree_from_file


def print_menu():
    print()
    print("---- Tree Notes ----")
    print("1. view all trees")
    print("2. new tree")
    print("3. exit")
    print()


def new_node(keys):
    print()
    print("$ Node: ")

    while True:
        print('- key(must be number): ', end='')
        my_key = int(input())

        if my_key == -1:
            return

        if not (my_key in keys):
            break
        else:
            print("key exists")

    print('- title: ', end='')
    my_title = input()

    print('- description: ', end='')
    my_description = input()

    return Node(my_key, my_title, my_description)


def edit_node():
    print()
    print("$ Node: ")

    print('- title: ', end='')
    my_title = input()

    print('- description: ', end='')
    my_description = input()

    return Node(-1, my_title, my_description)


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
                    my_node.description = temp_node.description
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

    my_root = Node(0, 'sample subject', 'sample description')
    my_tree = Tree(tree_name, my_root)

    print()
    print("Are you shure to create? (yes) ", end='')
    command = input()
    if command == 'yes':
        my_tree.write_tree_in_file()


def main_loop():
    while True:
        print_menu()
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
