from collections import Counter

class Tree:
    def __init__(self, name, height, age):
        self.name = name
        self.height = int(height)
        self.age = int(age)


class Trees:
    def __init__(self):
            self.trees = []

    def cut_trees(self, tree_age):
        self.trees = [tree for tree in self.trees if tree.age >= tree_age]

    def count_trees(self):
        return len(self.trees)

    def add_tree(self,tree):
        self.trees.append(tree)


#create a list of trees with name, height ,age data
forest = Trees()
forest.add_tree(Tree("oakwood", 134, 45))
forest.add_tree(Tree("orange", 120, 55))
forest.add_tree(Tree("mango", 14, 145))

#cut trees if age is greater than
forest.cut_trees(100)
print("Number of trees after cutting: ", forest.count_trees())
for tree in forest.trees:
    print(f"Tree name is {tree.name}", f"Tree height is {tree.height}m", f"Tree age is {tree.age}")

# print(forest.Trees.name())


    





    