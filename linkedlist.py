# Node class representing each student record
class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


# Linked List class to manage student records
class StudentLinkedList:
    def __init__(self):
        self.head = None

    # Add a new student record
    def add_student(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"\n✅ Student '{name}' added successfully!")

    # Delete a student by roll number
    def delete_student(self, roll_no):
        temp = self.head

        if temp is None:
            print("\n⚠️ No records to delete.")
            return

        if temp.roll_no == roll_no:
            self.head = temp.next
            print(f"\n❌ Student with Roll No {roll_no} deleted successfully!")
            return

        prev = None
        while temp and temp.roll_no != roll_no:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"\n⚠️ Roll No {roll_no} not found.")
            return

        prev.next = temp.next
        print(f"\n❌ Student with Roll No {roll_no} deleted successfully!")

    # Update student details
    def update_student(self, roll_no, new_name=None, new_marks=None):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                if new_name:
                    temp.name = new_name
                if new_marks is not None:
                    temp.marks = new_marks
                print(f"\n✏️ Student with Roll No {roll_no} updated successfully!")
                return
            temp = temp.next
        print(f"\n⚠️ Roll No {roll_no} not found.")

    # Search student by roll number
    def search_student(self, roll_no):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                print("\n🔍 Student Found:")
                print("----------------------------")
                print(f"Roll No: {temp.roll_no}")
                print(f"Name: {temp.name}")
                print(f"Marks: {temp.marks}")
                print("----------------------------")
                return
            temp = temp.next
        print(f"\n⚠️ Student with Roll No {roll_no} not found.")

    # Sort records based on roll number or marks
    def sort_records(self, by="roll", ascending=True):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if by == "roll":
                    cond = (current.roll_no > current.next.roll_no) if ascending else (current.roll_no < current.next.roll_no)
                else:  # sort by marks
                    cond = (current.marks > current.next.marks) if ascending else (current.marks < current.next.marks)

                if cond:
                    # swap data
                    current.roll_no, current.next.roll_no = current.next.roll_no, current.roll_no
                    current.name, current.next.name = current.next.name, current.name
                    current.marks, current.next.marks = current.next.marks, current.marks
                    swapped = True
                current = current.next
        print(f"\n📊 Records sorted by {by} ({'Ascending' if ascending else 'Descending'}).")

    # Display all student records
    def display_students(self):
        if not self.head:
            print("\n📭 No student records found.")
            return

        print("\n📘 Student Records:")
        print("------------------------------------------------")
        print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
        print("------------------------------------------------")
        temp = self.head
        while temp:
            print(f"{temp.roll_no:<10}{temp.name:<20}{temp.marks:<10}")
            temp = temp.next
        print("------------------------------------------------")


# Main Menu
if __name__ == "__main__":
    sll = StudentLinkedList()

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Sort Records")
        print("6. Display All Students")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            sll.add_student(roll, name, marks)

        elif choice == '2':
            roll = int(input("Enter Roll No to delete: "))
            sll.delete_student(roll)

        elif choice == '3':
            roll = int(input("Enter Roll No to update: "))
            new_name = input("Enter new name (leave blank to keep same): ")
            new_marks_input = input("Enter new marks (leave blank to keep same): ")
            new_marks = float(new_marks_input) if new_marks_input else None
            sll.update_student(roll, new_name or None, new_marks)

        elif choice == '4':
            roll = int(input("Enter Roll No to search: "))
            sll.search_student(roll)

        elif choice == '5':
            print("\nSort by: 1. Roll No  2. Marks")
            sort_choice = input("Enter choice (1 or 2): ")
            order_choice = input("Sort order - Ascending (A) / Descending (D): ").upper()
            by = "roll" if sort_choice == '1' else "marks"
            ascending = True if order_choice == 'A' else False
            sll.sort_records(by, ascending)

        elif choice == '6':
            sll.display_students()

        elif choice == '7':
            print("\n👋 Exiting Student Record Management System. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please try again.")
