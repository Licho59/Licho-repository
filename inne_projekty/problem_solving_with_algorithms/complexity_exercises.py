import timeit
import random

'''# Devise an experiment to verify that the list index operator is O(1)
list_index = timeit.Timer("x[len(x)//2]", "from __main__ import x")

for j in range(100, 100001, 100):
    x = list(range(j))
    index_time = list_index.timeit(number=1000)
    print("%d, %10.6f" % (j, index_time)) # it confirms O(1) complexity
    
    
# Devise an experiment to verify that get item and set item are O(1) for dictionaries.
dict_get = timeit.Timer("x.get(len(x)//3)", "from __main__ import x")
print('\nChecking the complexity of getting item in dictionary.')

for i in range(100, 100001, 100):
    x = {j: 'lew' for j in range(i)}
    get_time = dict_get.timeit(number=1000)
    print("{0}, {1:10.6f}".format(i, get_time)) # it confirms O(1) complexity
    
dict_set = timeit.Timer("x.setdefault('lion_best')", "from __main__ import x")
print('\nChecking the complexity of setting item in dictionary.')

for i in range(100, 100001, 100):
    x = {j: 'lion' for j in range(i)}
    set_time = dict_set.timeit(number=1000)
    print("{0}, {1:10.6f}".format(i, set_time)) # it confirms O(1) complexity'''
    
# Devise an experiment that compares the performance of the del operator on lists and dictionaries.  
print('\nComparing the complexity del method in lists and dictionaries.\n')
def del_dict_items(x):
    # Insert the index
    random_index = random.randrange(len(x) - 1)
    try:
        del x[random_index]
    except KeyError:
        x.setdefault(random_index, None)
        del x[random_index]

t_list = timeit.Timer(
        "del x[random.randrange(len(x)-1)]", "from __main__ import random, x")
t_dict = timeit.Timer("del_dict_items(x)",
                          "from __main__ import random, x, del_dict_items")

print("i\t\tlist_del_time\t\tdict_del_time")
for i in range(10000, 100001, 1000):    
    x = list(range(i))
    list_del_time = t_list.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_del_time = t_dict.timeit(number=1000)
    print("%d %10.3f %20.3f" % (i, list_del_time, dict_del_time)) # deleting from dictionary is  a little faster - it is O(1) complexity when for list it is around O(log(n))
