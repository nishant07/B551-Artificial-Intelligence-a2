# Best Solutions shown by this program:
# k =3 solution: 3 time(in seconds): 0.065
# k =4 solution: 10 time(in seconds): 0.18
# k =5 solution: 28 time(in seconds): 0.27
# k =6 solution: 68 time(in seconds): 0.55
# k =7 solution: 152 time(in seconds): 1.18
# Approach - created totogram tree as per the requirements using class as tree and having variables as value and
# children.
# We have created a totogram by randomly generating a list of all elements required in the totogram with specified k
# and calculated the maximum distance between any two nodes of totogram.
# We run this procedure for 1000 times which will yield a certain solution.


#!/usr/bin/python
import random
import sys
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


k = sys.argv[1]
num_range = 1 + 3*(2**(int(k)-1)-1)
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