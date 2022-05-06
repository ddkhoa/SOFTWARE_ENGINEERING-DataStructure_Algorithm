class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def __repr__(self):
        return f"Node({self.data})"


class SingleLinkedList:
    def __init__(self):
        self.head = None
        return

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join(str(item) for item in self)

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError("Index out of range.")

        # yield pair (index,value) (0, ll[0]), (1, ll[1])...
        # for i, node in enumerate(self):
        #     if i == index:
        #         return node

        # or
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, data):

        if not 0 <= index < len(self):
            raise IndexError("Index out of range.")

        current = self.head
        for i in range(index):  # go to node at index
            current = current.next
        current.data = data

    def insert_tail(self, data):
        self.insert_nth(len(self), data)

    def insert_head(self, data):
        self.insert_nth(0, data)

    def insert_nth(self, index, data):
        # first, we check if the index is in range
        # we can insert new element at len-th position (next element of current last element)
        if not 0 <= index <= len(self):
            raise IndexError("Index out of range.")

        new_node = Node(data)

        # treat special cases
        # if the linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # if insert at 0-th position (the head)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # normal case
        current = self.head
        for _ in range(index - 1):  # go to node at index - 1
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index):
        if not 0 <= index < len(self):
            raise IndexError("Index out of range.")

        # delete the head
        if index == 0:
            delete_node = self.head
            self.head = self.head.next
            return delete_node.data

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        current = prev.next
        prev.next = current.next
        return current.data

    def is_empty(self):
        return self.head is None

    def reverse(self):

        # we use 2 value: the previous node and the current node
        # iterate through the single linked list, for each element, we modify the next pointer to the previous node
        # in the end: prev = the last node, current = prev.next = None, we set the prev = head of the linked list
        prev = None
        current = self.head

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


def test_single_linked_list():
    """
    >>> test_singly_linked_list()
    """
    linked_list = SingleLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))

    assert all(linked_list[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        linked_list[i] = -i
    assert all(linked_list[i] == -i for i in range(0, 9)) is True

    linked_list.reverse()
    assert str(linked_list) == "->".join(str(i) for i in range(-8, 1))

    print("Test Single Linked List OK")


if __name__ == "__main__":
    test_single_linked_list()
