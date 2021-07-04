"""
  enumerate :  In built function accepts collection or tuples as inputs
  and output is an enumerated object with counter for each iterable object
"""


mylist = ['A', 'B' ,'C', 'D']
e_list = enumerate(mylist)
print(list(e_list))

for i in enumerate(mylist):
    print(i)

for i in enumerate(mylist,10):
    print(i)


my_tuple = ("A", "B", "C", "D", "E")
for i in enumerate(my_tuple):
  print(i)


grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
  print('{:05}_{}'.format(count, item))

for count, item in enumerate(grocery, 100):
  print( item)  


def even_items(iterable):
    """Return items from ``iterable`` when their index is even."""
    values = []
    for index, value in enumerate(iterable, start=1):
      if not index % 2:
         values.append(value)
    return values

def even_items_short(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]


seq = list(range(1, 11))

print(seq)
print(even_items(seq))
print(even_items_short(seq))

alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet)
print(even_items_short(alphabet))



first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
for one, two, three in zip(first, second, third):
    print(one, two, three)

for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three)
import itertools
for count, one, two, three in zip(itertools.count(), first, second, third):
    print(count, one, two, three)


step = 3
for i, name in enumerate(first):
    print(i * step, name)
