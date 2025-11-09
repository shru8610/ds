from collections import deque

class EventSystem:
    def __init__(self):
        self.event_queue = deque()  # Using deque for efficient queue operations

    # Add a new event to the queue
    def add_event(self, event_name):
        self.event_queue.append(event_name)
        print(f"\n Event '{event_name}' added to the queue.")

    # Process the next (oldest) event
    def process_next_event(self):
        if not self.event_queue:
            print("\n No events to process!")
            return
        event = self.event_queue.popleft()
        print(f"\n Processing event: '{event}' ... Done!")

    # Display all pending events
    def display_pending_events(self):
        if not self.event_queue:
            print("\n No pending events.")
        else:
            print("\n Pending Events in Queue:")
            print("----------------------------")
            for i, event in enumerate(self.event_queue, start=1):
                print(f"{i}. {event}")
            print("----------------------------")

    # Cancel an event that has not been processed yet
    def cancel_event(self, event_name):
        if event_name in self.event_queue:
            self.event_queue.remove(event_name)
            print(f"\n Event '{event_name}' has been canceled.")
        else:
            print(f"\n Event '{event_name}' not found or already processed.")


# Main Program
if __name__ == "__main__":
    system = EventSystem()

    while True:
        print("\n=== Real-Time Event Processing System ===")
        print("1. Add an Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            event = input("Enter event name: ")
            system.add_event(event)
        elif choice == '2':
            system.process_next_event()
        elif choice == '3':
            system.display_pending_events()
        elif choice == '4':
            event = input("Enter event name to cancel: ")
            system.cancel_event(event)
        elif choice == '5':
            print("\n Exiting Event Processing System. Goodbye!")
            break
        else:
            print("\n Invalid choice! Please try again.")
