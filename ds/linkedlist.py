from ds.node import Node
from ds.nodeiterator import NodeIterator

# naming conventions:
# https://www.realpythonproject.com/day20-variable-naming-conventions-in-python/

# only the class is exported
__all__ = ['LinkedList']


class LinkedList:
    def __init__(self):
        self.__length = 0
        self.__head = Node(None)

    def length(self):
        return self.__length

    def __validate(self, n):
        if n >= self.__length:
            raise Exception(f'{n} is out of range, valid range [0, {self.__length - 1}]')

    def at(self, n):
        self.__validate(n)
        return self.__at(n).data

    def __at(self, n):
        if n == -1:
            return self.__head
        i = 0
        cur = self.__head.next
        while i < n and cur is not None:
            cur = cur.next
            i += 1
        return cur

    def append(self, data):
        tail = self.__at(self.__length - 1)
        self.__append(tail, data)

    def appends(self, items):
        tail = self.__at(self.__length - 1)
        for item in items:
            tail = self.__append(tail, item)

    def __append(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        self.__length += 1
        return new_node

    # remove the node after
    def __remove_after(self, node):
        if node.next is not None:
            node.next = node.next.next
            self.__length -= 1

    # after insertion, data is at the nth position
    def insert(self, n, data):
        cur = self.__at(n - 1)
        if cur is None:
            raise Exception(f'position {n} is out of range')
        self.__append(cur, data)

    def remove(self, n):
        self.__validate(n)
        self.__remove_after(self.__at(n - 1))

    def __iter__(self):
        return NodeIterator(self.__head.next)

    def __str__(self):
        string_values = [str(i) for i in self]
        return " ".join(string_values)


class LinkedListIterator:
    def __init__(self, head):
        self.__cur = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur is not None:
            cur = self.__cur
            self.__cur = cur.next
            return cur.data
        else:
            raise StopIteration

