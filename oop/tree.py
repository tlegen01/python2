class MyTree:
    def __init__(self, name):
        self.age = 1
        self.name = name

    def drow(self, value_): #рост дерева
        self.age += value_

    @staticmethod
    def drow_static(value_: float, name: str):
        age = 1
        age += value_
        # tree = {"name": name, "age": age}
        # return tree
        return dict(name=name, age=age)

tree1 = MyTree("Дерево1")
print('возвраст ', tree1.name, "=", tree1.age)
tree1.drow(2)
print('возвраст ', tree1.name, "=", tree1.age)
tree2 = MyTree("Дерево2")
print('возвраст ', tree2.name, "=", tree2.age)

print(MyTree.drow_static(0, "derevo3")["age"])

#имя дерева: "дерево 3", возвраст дерева: "3"
tree_dict = MyTree.drow_static(2, "Дерево3")
print(tree_dict)
print(f"имя дерева: '{tree_dict['name']}', возвраст дерева:'{tree_dict['age']}'")