class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function using division method
    def hash_function(self, key):
        return key % self.size

    # Insert a key into the hash table
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == key:
                print(f"\n Key {key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("\n Hash table is full. Cannot insert new key.")
                return

        self.table[index] = key
        print(f"\n✅ Key {key} inserted at index {index}.")

    # Search for a key in the hash table
    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"\nKey {key} found at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break

        print(f"\n Key {key} not found in the table.")

    # Delete a key from the hash table
    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = "DELETED"
                print(f"\n❌ Key {key} deleted from index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break

        print(f"\n Key {key} not found. Cannot delete.")

    # Display the hash table
    def display(self):
        print("\n Hash Table Contents:")
        print("----------------------------")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print("----------------------------")


# Main program
if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\n=== Hash Table Operations ===")
        print("1. Insert Key")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            hash_table.insert(key)

        elif choice == '2':
            key = int(input("Enter key to search: "))
            hash_table.search(key)

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            hash_table.delete(key)

        elif choice == '4':
            hash_table.display()

        elif choice == '5':
            print("\n Exiting Hash Table Program. Goodbye!")
            break

        else:
            print("\n Invalid choice! Please try again.")
