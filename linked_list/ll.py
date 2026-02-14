arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data, position=None):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        if position is None:
            self.add_last(data)
            return

        if position == 0:
            self.add_first(data)
            return

        current_node = self.head
        current_position = 0

        while current_node.get_next() and current_position < position - 1:
            current_node = current_node.get_next()
            current_position += 1

        new_node.set_next(current_node.get_next())
        current_node.set_next(new_node)

    def add_first(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.get_next():
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def remove(self, key):
        current_node = self.head
        previous_node = None

        while current_node.get_next() and current_node.get_data() != key:
            previous_node = current_node
            current_node = current_node.get_next()

        if current_node.get_data() != key:
            return

        if not previous_node:
            self.head = current_node.get_next()  # Deleting the head node
        else:
            previous_node.set_next(current_node.get_next())  # Bypass the node to delete

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.get_data())
            current_node = current_node.get_next()
        print(" -> ".join(map(str, elements)))


linked_list = LinkedList()

for num in arr:
    linked_list.add_last(num)

linked_list.add_first(7)
linked_list.add_first(17)
linked_list.remove(9)
linked_list.display()
