class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # def delete(self, val):
    #     if val < self.data:
    #         if self.left:
    #             self.left = self.left.delete(val)

    #     elif val > self.data:
    #         if self.right:
    #             self.right = self.right.delete(val)

    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         elif self.left is None:
    #             return self.right
    #         elif self.right is None:
    #             return self.left

    #         min_val = self.find_min()
    #         self.data = min_val
    #         self.right = self.right.delete(min_val)
    #     return self

    def delete2(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete2(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete2(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.find_max()
            self.data = max_val
            self.left = self.left.delete2(max_val)
        return self

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    # def calculate_sum(self):
    #     elements = self.in_order_traversal()
    #     return sum(elements)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data


def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    number_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:\n ",
          number_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:\n ",
          number_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:\n ",
          number_tree.post_order_traversal())
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.calculate_sum())
    # number_tree.delete(23)
    number_tree.delete2(23)
    print("After deleting:\n ",
          number_tree.in_order_traversal())

    countries = ["India", "Pakistan", "Germany",
                 "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
