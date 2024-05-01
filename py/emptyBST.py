class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            node = self.root
            while node:
                if key < node.key:
                    if node.left is None:
                        node.left = TreeNode(key, value)
                        break
                    else:
                        node = node.left
                elif key > node.key:
                    if node.right is None:
                        node.right = TreeNode(key, value)
                        break
                    else:
                        node = node.right
                else:
                    node.value = value
                    break
    
    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def max_comparisons(self):
        node = self.root
        max_depth = 0
        stack = []
        while node or stack:
            if node:
                stack.append((node, 1))
                node = node.left
            else:
                node, depth = stack.pop()
                max_depth = max(max_depth, depth)
                node = node.right
        return max_depth

# Main program
bst = BinarySearchTree()
while True:
    print("\nDictionary Management System")
    print("1. Add Keyword and Meaning")
    print("2. Search for Keyword")
    print("3. Maximum Comparisons Required")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        keyword = input("Enter Keyword: ")
        meaning = input("Enter Meaning: ")
        bst.insert(keyword, meaning)
        print("Keyword added successfully.")
    elif choice == '2':
        keyword = input("Enter Keyword to search: ")
        result = bst.search(keyword)
        if result:
            print(f"Meaning: {result.value}")
        else:
            print("Keyword not found.")
    elif choice == '3':
        print("Maximum Comparisons Required:", bst.max_comparisons())
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
