# Node class to represent each element in the linked list.
# Each node contains data and a reference (link) to the next node.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value in the node
        self.next = None  # Pointer to the next node, initially None

# LinkedList class to manage the linked list operations.
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None (empty list)

    # Insert a new node at the beginning of the list.
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    # Insert a new node at the end of the list.
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, set head to the new node
            self.head = new_node
            return
        current = self.head  # Start from the head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Set the last node's next to the new node

    # Insert a new node at a specific position (0-based index).
    def insert_at_position(self, data, position):
        if position < 0:  # Invalid position
            print("Position cannot be negative.")
            return
        new_node = Node(data)  # Create a new node
        if position == 0:  # Insert at the beginning if position is 0
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:  # Traverse to the node before the position
            current = current.next
            count += 1
        if current is None:  # If position is beyond the list length
            print("Position out of range.")
            return
        new_node.next = current.next  # Insert the new node
        current.next = new_node

    # Delete the node at the beginning of the list.
    def delete_at_beginning(self):
        if self.head is None:  # If list is empty, nothing to delete
            print("List is empty.")
            return
        self.head = self.head.next  # Move head to the next node

    # Delete the node at the end of the list.
    def delete_at_end(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next is None:  # If only one node
            self.head = None
            return
        current = self.head
        while current.next.next:  # Traverse to the second last node
            current = current.next
        current.next = None  # Remove the last node

    # Delete the first node with the given data value.
    def delete_by_value(self, data):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.data == data:  # If head node has the value
            self.head = self.head.next
            return
        current = self.head
        while current.next:  # Traverse to find the node
            if current.next.data == data:
                current.next = current.next.next  # Remove the node
                return
            current = current.next
        print("Value not found.")  # If value not in list

    # Search for a node with the given data and return True if found.
    def search(self, data):
        current = self.head
        while current:  # Traverse the list
            if current.data == data:
                return True  # Found
            current = current.next
        return False  # Not found

    # Print all elements in the list.
    def print_list(self):
        current = self.head
        while current:  # Traverse and print each node's data
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list

    # Get the length (number of nodes) in the list.
    def length(self):
        count = 0
        current = self.head
        while current:  # Traverse and count
            count += 1
            current = current.next
        return count

    # Reverse the linked list.
    def reverse(self):
        prev = None
        current = self.head
        while current:  # Traverse and reverse pointers
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev  # Update head to the new first node

# Example usage:
# Create a linked list
ll = LinkedList()

# Insert operations
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_position(15, 1)  # Insert 15 between 10 and 20

# Print the list: 10 -> 15 -> 20 -> None
ll.print_list()

# Search for 15: True
print(ll.search(15))

# Delete operations
ll.delete_at_beginning()  # Removes 10
ll.delete_at_end()  # Removes 20
ll.delete_by_value(15)  # Removes 15

# Print the list after deletions: None
ll.print_list()

# Length: 0
print(ll.length())

# Insert again and reverse
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.print_list()  # 30 -> 40 -> 50 -> None
ll.reverse()
ll.print_list()  # 50 -> 40 -> 30 -> None
