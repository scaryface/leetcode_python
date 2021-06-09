class Node:
    def __init__(self, key=-1, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:

    # with sentinel handling edge cases (head and tail of a linked list) is easy
    def __init__(self):
        self.__sentinel__ = Node()
        self.__sentinel__.next = self.__sentinel__
        self.__sentinel__.prev = self.__sentinel__
    
    # insert is O(1) because of using sentinel
    def insert(self, key):
        node = Node(key)
        self.__sentinel__.prev.next = node
        node.prev = self._sentinel__.prev
        node.next = self.__sentinel__
        self.__sentinel__.prev = node
        return self.__sentinel__.next


    def delete(self, node):
        if not node and not node.prev and not node.next:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        return self.__sentinel__.next

    