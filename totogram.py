#!/usr/bin/python
import random


def get_list_element():
    chosen_value = random.choice(alist)
    alist.remove(chosen_value)
    return chosen_value


def create_tree():
    root = Tree(get_list_element())
    root.children.append(Tree(get_list_element()))
    children_list.append(root.children[0])
    root.children.append(Tree(get_list_element()))
    children_list.append(root.children[1])
    root.children.append(Tree(get_list_element()))
    children_list.append(root.children[2])
    while True:
        try:
            data = get_list_element()
        except IndexError:
            return root
        #insert(children_list[0], Tree(data))
        childNode = children_list[0]
        if not (len(childNode.children) > 0):
            childNode.children.append(Tree(data))
            children_list.append(childNode.children[0])
        else:
            childNode.children.append(Tree(data))
            children_list.append(childNode.children[1])
            children_list.pop(0)
    return root


def total(tree):
    if tree is None:
        return 0
    return total(tree.left) + total(tree.right) + tree.value


def print_tree(tree):
    print_list = []
    answer = ""
    max_diff = 0
    print_list.append(tree)
    while len(print_list) > 0:
        for child in print_list[0].children:
            diff = (print_list[0].value - child.value)
            if diff < 0:
                diff *= -1
            if max_diff < diff:
                max_diff = diff
            print_list.append(child)
        answer += str(print_list[0].value) + " "
        print_list.pop(0)
    print max_diff
    print answer


class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []


k = 7
num_range = 1 + 3*(2**(k-1)-1)
alist = range(num_range+1)
alist.remove(0)
children_list = []
root = None
root = create_tree()
print_tree(root)
