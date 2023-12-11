class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def display_linked_list(head):
        if head.next == None:
            return head.value

        full_list = []
        while head.next != None:
            full_list.append(head.value)

        return full_list


# Test your implementation
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

Node.display_linked_list(node1)
