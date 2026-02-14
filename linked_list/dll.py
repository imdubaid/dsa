arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, next):
        self.__next = next

    def set_prev(self, prev):
        self.__prev = prev


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data, position=None):
        new_node = Node(data)

        if position is None:
            self.add_last(data)
            return

        if position == 0 or not self.head:
            self.add_first(data)
            return

        current_node = self.head
        current_position = 0

        while current_node.get_next() and current_position < position - 1:
            current_node = current_node.get_next()
            current_position += 1

        if not current_node.get_next():
            self.add_last(data)
            return

        next_node = current_node.get_next()

        new_node.set_prev(current_node)
        new_node.set_next(next_node)

        current_node.set_next(new_node)
        next_node.set_prev(new_node)

    def add_first(self, data):
        new_node = Node(data, prev=None, next=self.head)

        if self.head:
            self.head.set_prev(new_node)

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
        new_node.set_prev(current_node)

    def remove(self, key):
        current_node = self.head

        while current_node and current_node.get_data() != key:
            current_node = current_node.get_next()

        if not current_node:
            return

        prev_node = current_node.get_prev()
        next_node = current_node.get_next()

        if not prev_node:
            self.head = next_node
            if self.head:
                self.head.set_prev(None)
        else:
            prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)

    def display(self, order=None):
        elements = []

        if order == "reverse":
            current_node = self.head

            if not current_node:
                print("")
                return

            while current_node.get_next():
                current_node = current_node.get_next()

            while current_node:
                elements.append(current_node.get_data())
                current_node = current_node.get_prev()
        else:
            current_node = self.head
            while current_node:
                elements.append(current_node.get_data())
                current_node = current_node.get_next()

        print(" <--> ".join(map(str, elements)))

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.get_data())
            current_node = current_node.get_next()
        print(" <--> ".join(map(str, elements)))


linked_list = LinkedList()

for num in arr:
    linked_list.add(num)

linked_list.add_first(7)
linked_list.add_first(17)
linked_list.add(15, 5)
linked_list.remove(19)
linked_list.display()
