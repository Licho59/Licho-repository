from timeit import timeit
from unordered_complete_linkedList import LinkedList

linked_list = LinkedList()
ll = timeit(lambda: linked_list.add(0), number=10**5)
#0.08297442221169149

python_list = []
pl = timeit(lambda: python_list.insert(0, 0), number=10**5)
#1.5988611595369093

print("Linkedlist ", ll)
print("Python list ", pl)
