# Node structure for Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Binary Search Tree Class
class BST:
    def __init__(self):
        self.root = None

    # Insert a key into BST
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            print(f"Inserted {key}")
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            print(f"Key {key} already exists!")
        return root

    # Search for a key in BST
    def search(self, key):
        found = self._search(self.root, key)
        if found:
            print(f" Key {key} found in the BST.")
        else:
            print(f" Key {key} not found.")
        return found

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # Delete a key from BST
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            print(f"⚠️ Key {key} not found. Nothing to delete.")
            return root

        # Traverse to find the node
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node found — handle 3 cases
            if root.left is None:
                print(f"🗑️ Deleted {key}")
                return root.right
            elif root.right is None:
                print(f"🗑️ Deleted {key}")
                return root.left

            # Node with 2 children — find inorder successor
            min_node = self._min_value_node(root.right)
            root.key = min_node.key
            root.right = self._delete(root.right, min_node.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Display the tree
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":
    bst = BST()

    while True:
        print("\n=== Binary Search Tree Operations ===")
        print("1. Insert a Node")
        print("2. Search a Node")
        print("3. Delete a Node")
        print("4. Display Tree")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter value to insert: "))
            bst.insert(key)

        elif choice == '2':
            key = int(input("Enter value to search: "))
            bst.search(key)

        elif choice == '3':
            key = int(input("Enter value to delete: "))
            bst.delete(key)

        elif choice == '4':
            print("\nInorder Traversal: ", end="")
            bst.inorder(bst.root)
            print("\nPreorder Traversal: ", end="")
            bst.preorder(bst.root)
            print("\nPostorder Traversal: ", end="")
            bst.postorder(bst.root)
            print()

        elif choice == '5':
            print("\n Exiting program. Goodbye!")
            break

        else:
            print("\n Invalid choice! Please try again.")
