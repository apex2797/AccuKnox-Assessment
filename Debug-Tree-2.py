def parent_tree(root, tree, indent_width=4): # 4 is correctly alligning with parents

    def printer(root, parent, tree, space=""):
        print(parent)
        # makes sure the values are in the tree (data) if not returning.
        # also make sures the children is next parent
        if parent in tree:
            for child in tree[parent][:-1]:
                print(space + "├" + "─" * indent_width, end="")
                # basically makes a space_gap if its a child.
                printer(root, child, tree,  space + "|" + " " * 4)
        else:
            return

        # for loop misses the last value so, --
        child = tree[parent][-1]
        print(space + '└' + "─" * indent_width, end="")
        # makes a empty space
        printer(root, child, tree, space + " " * 5) # 5 makes the space connected with parent.

    parent = root
    printer(root, parent, tree)

tree_1 = {
    'root':[1,2,3],
    1 :[1.1, 1.2, 1.3, 1.4, 1.5],
    2 :[2.1, 2.2, 2.3, 2.4, 2.5],
    3 :[3.1, 3.2,3.5],
    3.5:[3.5855, 3.5999]
}
tree_2 = {
    'Class':['robot', 'human'],
    'robot':['charge', 'battery', 'commands', 'Grrrbb'],
    'human':['love', 'food', 'sleep', 'nature'],
    'nature':['Mountain' , 'forest'],
    'Grrrbb':[1001, 10110]
}

parent_tree('root', tree_1)
print('Data Tree is Fun!!', end='\n')
parent_tree('Class', tree_2)



