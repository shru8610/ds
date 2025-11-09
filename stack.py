# Text Editor Undo/Redo system using Stack

class TextEditor:
    def __init__(self):
        self.text = ""                # Current document text
        self.undo_stack = []          # Stack to store changes for undo
        self.redo_stack = []          # Stack to store undone changes for redo

    # Make a new change
    def make_change(self, new_text):
        self.undo_stack.append(self.text)  # Save current state before change
        self.text = new_text               # Apply new text
        self.redo_stack.clear()            # Clear redo stack after new change
        print("\n Change made successfully!")

    # Undo last action
    def undo(self):
        if not self.undo_stack:
            print("\n No actions to undo!")
            return
        self.redo_stack.append(self.text)   # Save current text for redo
        self.text = self.undo_stack.pop()   # Revert to previous state
        print("\n↩ Undo performed successfully!")

    # Redo last undone action
    def redo(self):
        if not self.redo_stack:
            print("\n No actions to redo!")
            return
        self.undo_stack.append(self.text)   # Save current text for undo
        self.text = self.redo_stack.pop()   # Reapply last undone text
        print("\n Redo performed successfully!")

    # Display current document text
    def display(self):
        print("\nCurrent Document State:")
        print("--------------------------")
        print(self.text if self.text else "[Empty Document]")
        print("--------------------------")


# Main program
if __name__ == "__main__":
    editor = TextEditor()

    while True:
        print("\n=== Text Editor Menu ===")
        print("1. Make a Change")
        print("2. Undo Last Action")
        print("3. Redo Last Action")
        print("4. Display Document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            new_text = input("Enter new text: ")
            editor.make_change(new_text)
        elif choice == '2':
            editor.undo()
        elif choice == '3':
            editor.redo()
        elif choice == '4':
            editor.display()
        elif choice == '5':
            print("\n Exiting Text Editor... Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")
