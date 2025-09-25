# Node class for a doubly linked list.
# Each node contains data, a reference to the next node, and a reference to the previous node.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value in the node
        self.next = None  # Pointer to the next node, initially None
        self.prev = None  # Pointer to the previous node, initially None

# DoublyLinkedList class to manage doubly linked list operations.
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None (empty list)

    # Insert a new node at the beginning of the list.
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head:
            self.head.prev = new_node  # Set current head's prev to new node
            new_node.next = self.head  # Set new node's next to current head
        self.head = new_node  # Update head to the new node

    # Insert a new node at the end of the list.
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, set head to new node
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Set last node's next to new node
        new_node.prev = current  # Set new node's prev to last node

    # Insert a new node at a specific position (0-based index).
    def insert_at_position(self, data, position):
        if position < 0:  # Invalid position
            print("Position cannot be negative.")
            return
        new_node = Node(data)  # Create a new node
        if position == 0:  # Insert at beginning if position is 0
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:  # Traverse to node before position
            current = current.next
            count += 1
        if current is None:  # If position is beyond list length
            print("Position out of range.")
            return
        new_node.next = current.next  # Set new node's pointers
        new_node.prev = current
        if current.next:  # Update next node's prev pointer if it exists
            current.next.prev = new_node
        current.next = new_node  # Update current node's next pointer

    # Delete the node at the beginning of the list.
    def delete_at_beginning(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        self.head = self.head.next  # Move head to next node
        if self.head:  # Update prev pointer of new head
            self.head.prev = None

    # Delete the node at the end of the list.
    def delete_at_end(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next is None:  # If only one node
            self.head = None
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.prev.next = None  # Set second last node's next to None

    # Delete the first node with the given data value.
    def delete_by_value(self, data):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.data == data:  # If head node has the value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current:  # Traverse to find the node
            if current.data == data:
                if current.next:  # Update next node's prev pointer
                    current.next.prev = current.prev
                current.prev.next = current.next  # Update prev node's next pointer
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

    # Print all elements in the list (forward).
    def print_list_forward(self):
        current = self.head
        while current:  # Traverse and print each node's data
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # End of list

    # Print all elements in the list (backward).
    def print_list_backward(self):
        if self.head is None:
            print("None")
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        while current:  # Traverse backward and print
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")  # End of list

    # Get the length (number of nodes) in the list.
    def length(self):
        count = 0
        current = self.head
        while current:  # Traverse and count
            count += 1
            current = current.next
        return count

    # Reverse the doubly linked list.
    def reverse(self):
        if self.head is None or self.head.next is None:  # If empty or single node
            return
        current = self.head
        while current:  # Traverse and swap next/prev pointers
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        self.head = self.head.prev  # Update head to last node

# Example usage:
# Create a doubly linked list
dll = DoublyLinkedList()

# Insert operations
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_position(15, 1)  # Insert 15 between 10 and 20

# Print forward: 10 <-> 15 <-> 20 <-> None
dll.print_list_forward()

# Print backward: 20 <-> 15 <-> 10 <-> None
dll.print_list_backward()

# Search for 15: True
print(dll.search(15))

# Delete operations
dll.delete_at_beginning()  # Removes 10
dll.delete_at_end()  # Removes 20
dll.delete_by_value(15)  # Removes 15

# Print forward after deletions: None
dll.print_list_forward()

# Length: 0
print(dll.length())

# Insert again and reverse
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.print_list_forward()  # 30 <-> 40 <-> 50 <-> None
dll.reverse()
dll.print_list_forward()  # 50 <-> 40 <-> 30 <-> None
