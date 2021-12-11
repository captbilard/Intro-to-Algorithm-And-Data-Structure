class Node:
    """
    An object for storing a single node of a linked list. Models two attributes
    data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class Linked_List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds data to the Head of the list.
        Takes O(n) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return None
    
    def search(self, key):
        current = self.head

        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node  
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at the index position
        Insertion takes O(1) (constant time) but finding the node at the
        insertion points takes O(n) time.
        Takes overall O(n) time
        """
        if index == 0:
            return self.add(data)
        
        new_node = Node(data)
        current  = self.head

        position = index

        while position > 1:
            current = current.next_node
            position -= 1
        
        prev_node = current.next_node
        new_node.next_node = prev_node
        current.next_node = new_node 


    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current == self.head:
                nodes.append(f'[Head: {current.data}]')
            elif current.next_node == None:
                nodes.append(f'[Tail: {current.data}]')
            else:
                nodes.append(f'[{current.data}]')
            
            current = current.next_node
        return "-> ".join(nodes)
