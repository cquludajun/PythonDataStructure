from ds import LinkedList

linked_list = LinkedList()

for i in range(0, 10):
    linked_list.append(str(i))

print(linked_list)

linked_list.appends(range(10, 20))

print(linked_list)
