# Node class to represent each element in the circular singly linked list.
# Each node contains data and a reference to the next node.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value in the node
        self.next = None  # Pointer to the next node, initially None

# CircularSinglyLinkedList class to manage circular singly linked list operations.
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None (empty list)

    # Insert a new node at the beginning of the list.
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If list is empty
            self.head = new_node
            new_node.next = self.head  # Point to itself to form a circle
            return
        current = self.head
        while current.next != self.head:  # Traverse to the last node
            current = current.next
        new_node.next = self.head  # New node points to current head
        current.next = new_node  # Last node points to new node
        self.head = new_node  # Update head to new node

    # Insert a new node at the end of the list.
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If list is empty
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        current = self.head
        while current.next != self.head:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Last node points to new node
        new_node.next = self.head  # New node points to head to maintain circularity

    # Insert a new node at a specific position (0-based index).
    def insert_at_position(self, data, position):
        if position < 0:  # Invalid position
            print("Position cannot be negative.")
            return
        new_node = Node(data)  # Create a new node
        if position == 0:  # Insert at beginning
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 0
        while current and count < position - 1 and current.next != self.head:  # Traverse to node before position
            current = current.next
            count += 1
        if current is None or current.next == self.head and count < position - 1:  # If position is beyond list length
            print("Position out of range.")
            return
        new_node.next = current.next  # Insert new node
        current.next = new_node

    # Delete the node at the beginning of the list.
    def delete_at_beginning(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next == self.head:  # If only one node
            self.head = None
            return
        current = self.head
        while current.next != self.head:  # Traverse to the last node
            current = current.next
        self.head = self.head.next  # Move head to next node
        current.next = self.head  # Update last node's next to new head

    # Delete the node at the end of the list.
    def delete_at_end(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next == self.head:  # If only one node
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:  # Traverse to second last node
            current = current.next
        current.next = self.head  # Update second last node's next to head

    # Delete the first node with the given data value.
    def delete_by_value(self, data):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.data == data:  # If head has the value
            self.delete_at_beginning()
            return
        current = self.head
        while current.next != self.head:  # Traverse to find the node
            if current.next.data == data:
                current.next = current.next.next  # Remove the node
                return
            current = current.next
        print("Value not found.")  # If value not in list

    # Search for a node with the given data and return True if found.
    def search(self, data):
        if self.head is None:  # If list is empty
            return False
        current = self.head
        while True:  # Traverse the circular list
            if current.data == data:
                return True  # Found
            current = current.next
            if current == self.head:  # Back to start, end loop
                break
        return False  # Not found

    # Print all elements in the list.
    def print_list(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        current = self.head
        while True:  # Traverse and print
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Back to start, end loop
                break
        print("(head)")  # Indicate circularity

    # Get the length (number of nodes) in the list.
    def length(self):
        if self.head is None:  # If list is empty
            return 0
        count = 0
        current = self.head
        while True:  # Traverse and count
            count += 1
            current = current.next
            if current == self.head:  # Back to start, end loop
                break
        return count

    # Reverse the circular singly linked list.
    def reverse(self):
        if self.head is None or self.head.next == self.head:  # If empty or single node
            return
        prev = None
        current = self.head
        tail = self.head
        while True:  # Traverse and reverse pointers
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:  # Back to start, end loop
                break
        self.head = prev  # Update head to last node
        tail.next = self.head  # Maintain circularity

# Example usage:
# Create a circular singly linked list
csll = CircularSinglyLinkedList()

# Insert operations
csll.insert_at_beginning(10)
csll.insert_at_end(20)
csll.insert_at_position(15, 1)  # Insert 15 between 10 and 20

# Print list: 10 -> 15 -> 20 -> (head)
csll.print_list()

# Search for 15: True
print(csll.search(15))

# Delete operations
csll.delete_at_beginning()  # Removes 10
csll.delete_at_end()  # Removes 20
csll.delete_by_value(15)  # Removes 15

# Print list after deletions: List is empty.
csll.print_list()

# Length: 0
print(csll.length())

# Insert again and reverse
csll.insert_at_end(30)
csll.insert_at_end(40)
csll.insert_at_end(50)
csll.print_list()  # 30 -> 40 -> 50 -> (head)
csll.reverse()
csll.print_list()  # 50 -> 40 -> 30 -> (head)
