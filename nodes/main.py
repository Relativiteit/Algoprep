from Node import Node

first = Node(5, None)

second = Node(6, first)

print("this is the first node", first)
print("This is the second node", second)

# you can't sum or minus nodes
answer_minus = first.value - second.value
answer_plus = first.value + second.value

print("I am trying to print a node", answer_minus)
print("I am trying to print a node", answer_plus)

next_pointer = second.next
print(next_pointer)

next_pointer_next = second.next.next

print(next_pointer_next)
