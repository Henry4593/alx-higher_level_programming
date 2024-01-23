#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data to be stored in the Node.
            next_node (Node, optional): The next Node in the list.
                                        Defaults to None.

        Raises:
            TypeError: If data is not an integer.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data stored in the Node."""

        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the Node, ensuring it's an integer.

        Args:
            value (int): The new data to set.

        Raises:
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next Node in the list."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next Node in the list, ensuring it's a Node object or None.

        Args:
            value (Node, None): The new next Node to set.

        Raises:
            TypeError: If value is not a Node object and not None.
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initializes a new, empty SinglyLinkedList."""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the SinglyLinkedList in sorted order.

        Args:
            value (int): The data to be stored in the new Node.

        Raises:
            TypeError: If value is not an integer.
        """

        new_node = Node(value)  # Create the new Node with the given value

        if self.__head is None:
            # If the list is empty, set the new Node as the head
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse the list to find the correct position for the new Node
            current = self.__head
            while (current.next_node is not None and current.next_node.data
                   < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Defines the print() representation of the SinglyLinkedList."""

        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
