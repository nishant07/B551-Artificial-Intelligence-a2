#!/usr/bin/python
import random
from copy import deepcopy


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


def calculate_tree(tree):
    cal_list = []
    max_diff = 0
    cal_list.append(tree)
    while len(cal_list) > 0:
        for cal_child in cal_list[0].children:
            cal_list.append(cal_child)
            diff = (cal_list[0].value - cal_child.value)
            if diff < 0:
                diff *= -1
            if max_diff < diff:
                max_diff = diff
        cal_list.pop(0)
    return max_diff


def print_tree(tree):
    print_list = []
    answer = ""
    print_list.append(tree)
    while len(print_list) > 0:
        for child in print_list[0].children:
            print_list.append(child)
        answer += str(print_list[0].value) + " "
        print_list.pop(0)
    return answer


def change_node_value(tree, old_value, new_value):
    change_list = []
    answer = ""
    change_list.append(tree)
    while len(change_list) > 0:
        for child in change_list[0].children:
            if child.value is old_value:
                child.value = new_value
                return
            change_list.append(child)
        change_list.pop(0)


def set_backup_tree(tree):
    global backup_tree
    backup_tree = None
    backup_tree = deepcopy(tree)


def get_backup_tree():
    global backup_tree
    return backup_tree


class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []


k = 3
num_range = 1 + 3*(2**(k-1)-1)
best_diff = num_range
best_tree = None
elem_list = range(num_range+1)
elem_list.remove(0)
backup_tree = None
for x in range(1000):
    alist = None
    alist = deepcopy(elem_list)
    children_list = []
    root = None
    root = create_tree()
    cal_diff = calculate_tree(root)
    result_tree = print_tree(root)
    if cal_diff < best_diff:
        best_diff = deepcopy(cal_diff)
        best_tree = deepcopy(root)
print best_diff
print print_tree(best_tree)