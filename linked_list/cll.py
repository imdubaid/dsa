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
            self.head.set_next(self.head)
            return

        if position is None:
            self.add_last(data)
            return

        if position == 0:
            self.add_first(data)
            return

        current_node = self.head
        current_position = 0

        while current_node.get_next() != self.head and current_position < position - 1:
            current_node = current_node.get_next()
            current_position += 1

        new_node.set_next(current_node.get_next())
        current_node.set_next(new_node)

    def add_first(self, data):
        new_node = Node(data, self.head)

        if not self.head:
            self.head = new_node
            self.head.set_next(self.head)
            return

        tail = self.head
        while tail.get_next() != self.head:
            tail = tail.get_next()
        tail.set_next(new_node)
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)  # Point to head to maintain circular structure

        if not self.head:
            self.head = new_node
            self.head.set_next(self.head)
            return

        current_node = self.head
        while current_node.get_next() != self.head:
            current_node = current_node.get_next()

        current_node.set_next(new_node)
        new_node.set_next(self.head)

    def remove(self, key):
        if not self.head:
            return

        current_node = self.head
        prev_node = None

        while True:
            if current_node.get_data() == key:
                # removing head
                if prev_node is None:
                    # single node case
                    if current_node.get_next() == self.head:
                        self.head = None
                        return

                    # find tail
                    tail = self.head
                    while tail.get_next() != self.head:
                        tail = tail.get_next()

                    self.head = current_node.get_next()
                    tail.set_next(self.head)
                else:
                    prev_node.set_next(current_node.get_next())
                return

            prev_node = current_node
            current_node = current_node.get_next()

            if current_node == self.head:
                return

    def display(self):
        elements = []
        current_node = self.head

        while current_node.get_next() != self.head:
            elements.append(current_node.get_data())
            current_node = current_node.get_next()

        elements.append(current_node.get_data())  # Add the last node's data
        print(" --> ".join(map(str, elements)))


linked_list = LinkedList()

for num in arr:
    linked_list.add_last(num)

linked_list.remove(17)
linked_list.add_first(7)
linked_list.add_first(17)
linked_list.remove(7)
linked_list.add_first(8)
linked_list.remove(9)
linked_list.display()
