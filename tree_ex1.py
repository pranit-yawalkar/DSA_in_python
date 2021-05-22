# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
# Creating a tree class
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, arg):

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|_" if self.parent else ""
        if arg == "name":
            print(prefix + self.name)

        elif arg == "designation":
            print(prefix + " (" + self.designation + ")")

        else:
            print(prefix + self.name + " (" + self.designation + ")")
        if self.children:
            for child in self.children:
                child.print_tree(arg)


def build_management_tree():
    nilpul = TreeNode("Nilpul", "CEO")

    chinmay = TreeNode("Chinmay", "CTO")

    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter", "Recruiter Manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))

    vishwa = TreeNode("Vishwa", "Infrastructure Head")
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))

    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Aamir", "App Manager"))

    nilpul.add_child(chinmay)
    nilpul.add_child(gels)
    return nilpul


if __name__ == "__main__":
    if __name__ == '__main__':
        root_node = build_management_tree()
        root_node.print_tree("name")  # prints only name hierarchy
        # prints only designation hierarchy
        root_node.print_tree("designation")
        # prints both (name and designation) hierarchy
        root_node.print_tree("both")
