class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|_" if self.parent else ""
        print(prefix + self.data)
        # if arg == 1:
        #     self.
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode("india")
    usa = TreeNode("USA")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bengaluru"))
    Karnataka.add_child(TreeNode("Mysore"))

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))

    india.add_child(gujarat)
    india.add_child(Karnataka)

    usa.add_child(nj)
    usa.add_child(cal)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree(3)
