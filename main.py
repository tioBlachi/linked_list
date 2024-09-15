class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data): # adds to end of linked list
        # if there is no data in list...
        new_node = Node(data)

        if self.head is None: # if the linked list is empty, head and tail are the new node
            self.head = new_node
            self.tail = new_node
            return

        else:
            self.tail.next = new_node # tail will point to the new node
            self.tail = new_node
            return


    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at(self, data, location):
        new_node = Node(data)
        if location == 0:
            self.insert_at_beginning(data)
            return

        current_node = self.head
        for _ in range(location - 1):
            if current_node is None:
                raise IndexError("Location out of bounds")
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next

    def print_list_reverse(self):
        current = self.head
        stack = []
        if self.tail is None:
            print("The list is empty")
            return
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=' -> ')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

llist = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.insert_at_beginning(5)
llist.insert_at_beginning(6)
llist.append(7)
llist.insert_at(40, 6)
llist.print_list()
print()
llist.print_list_reverse()