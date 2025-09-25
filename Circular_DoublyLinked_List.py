# Node class for a circular doubly linked list.
# Each node contains data, a reference to the next node, and a reference to the previous node.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value in the node
        self.next = None  # Pointer to the next node, initially None
        self.prev = None  # Pointer to the previous node, initially None

# CircularDoublyLinkedList class to manage circular doubly linked list operations.
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None (empty list)

    # Insert a new node at the beginning of the list.
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If list is empty
            self.head = new_node
            new_node.next = new_node  # Point to itself
            new_node.prev = new_node  # Point to itself
            return
        last = self.head.prev  # Get the last node
        new_node.next = self.head  # New node points to current head
        new_node.prev = last  # New node points back to last node
        self.head.prev = new_node  # Current head's prev points to new node
        last.next = new_node  # Last node's next points to new node
        self.head = new_node  # Update head to new node

    # Insert a new node at the end of the list.
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If list is empty
            self.head = new_node
            new_node.next = new_node  # Point to itself
            new_node.prev = new_node  # Point to itself
            return
        last = self.head.prev  # Get the last node
        new_node.next = self.head  # New node points to head
        new_node.prev = last  # New node points back to last node
        last.next = new_node  # Last node's next points to new node
        self.head.prev = new_node  # Head's prev points to new node

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
        while count < position - 1 and current.next != self.head:  # Traverse to node before position
            current = current.next
            count += 1
        if current.next == self.head and count < position - 1:  # If position is beyond list length
            print("Position out of range.")
            return
        new_node.next = current.next  # Set new node's pointers
        new_node.prev = current
        current.next.prev = new_node  # Update next node's prev
        current.next = new_node  # Update current node's next

    # Delete the node at the beginning of the list.
    def delete_at_beginning(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next == self.head:  # If only one node
            self.head = None
            return
        last = self.head.prev  # Get the last node
        self.head = self.head.next  # Move head to next node
        self.head.prev = last  # Update new head's prev to last node
        last.next = self.head  # Update last node's next to new head

    # Delete the node at the end of the list.
    def delete_at_end(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.next == self.head:  # If only one node
            self.head = None
            return
        last = self.head.prev  # Get the last node
        last.prev.next = self.head  # Second last node's next points to head
        self.head.prev = last.prev  # Head's prev points to second last node

    # Delete the first node with the given data value.
    def delete_by_value(self, data):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        if self.head.data == data:  # If head has the value
            self.delete_at_beginning()
            return
        current = self.head.next
        while current != self.head:  # Traverse to find the node
            if current.data == data:
                current.prev.next = current.next  # Update prev node's next
                current.next.prev = current.prev  # Update next node's prev
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

    # Print all elements in the list (forward).
    def print_list_forward(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        current = self.head
        while True:  # Traverse and print
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:  # Back to start, end loop
                break
        print("(head)")  # Indicate circularity

    # Print all elements in the list (backward).
    def print_list_backward(self):
        if self.head is None:  # If list is empty
            print("List is empty.")
            return
        last = self.head.prev
        current = last
        while True:  # Traverse backward and print
            print(current.data, end=" <-> ")
            current = current.prev
            if current == last:  # Back to start, end loop
                break
        print("(last)")  # Indicate circularity

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

    # Reverse the circular doubly linked list.
    def reverse(self):
        if self.head is None or self.head.next == self.head:  # If empty or single node
            return
        current = self.head
        while True:  # Traverse and swap next/prev pointers
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
            if current == self.head:  # Back to start, end loop
                break
        self.head = self.head.prev  # Update head to last node

# Example usage:
# Create a circular doubly linked list
cdll = CircularDoublyLinkedList()

# Insert operations
cdll.insert_at_beginning(10)
cdll.insert_at_end(20)
cdll.insert_at_position(15, 1)  # Insert 15 between 10 and 20

# Print forward: 10 <-> 15 <-> 20 <-> (head)
cdll.print_list_forward()

# Print backward: 20 <-> 15 <-> 10 <-> (last)
cdll.print_list_backward()

# Search for 15: True
print(cdll.search(15))

# Delete operations
cdll.delete_at_beginning()  # Removes 10
cdll.delete_at_end()  # Removes 20
cdll.delete_by_value(15)  # Removes 15

# Print forward after deletions: List is empty.
cdll.print_list_forward()

# Length: 0
print(cdll.length())

# Insert again and reverse
cdll.insert_at_end(30)
cdll.insert_at_end(40)
cdll.insert_at_end(50)
cdll.print_list_forward()  # 30 <-> 40 <-> 50 <-> (head)
cdll.reverse()
cdll.print_list_forward()  # 50 <-> 40 <-> 30 <-> (head)
