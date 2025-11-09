# Hash Table implementation using Chaining (Linked List)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # each slot contains a list for chaining

    # Hash function using Division Method
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists — update its value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with new value '{value}' at index {index}.")
                return
        # If key doesn't exist, append new pair
        self.table[index].append([key, value])
        print(f" Inserted ({key}, '{value}') at index {index}.")

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"🔍 Key {key} found at index {index} with value '{pair[1]}'.")
                return pair[1]
        print(f"Key {key} not found in the hash table.")
        return None

    # Delete a key
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f" Deleted key {key} from index {index}.")
                return
        print(f" Key {key} not found. Nothing to delete.")

    # Display the hash table
    def display(self):
        print("\n Hash Table Contents:")
        print("-" * 35)
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print("-" * 35)


# Main Program
if __name__ == "__main__":
    hash_table = HashTable(10)

    while True:
        print("\n=== Hash Table (Chaining) Menu ===")
        print("1. Insert Key-Value Pair")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key (integer): "))
            value = input("Enter value (string): ")
            hash_table.insert(key, value)

        elif choice == '2':
            key = int(input("Enter key to search: "))
            hash_table.search(key)

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            hash_table.delete(key)

        elif choice == '4':
            hash_table.display()

        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\n Invalid choice! Please enter a number between 1 and 5.")
