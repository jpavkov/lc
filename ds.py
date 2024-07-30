## purpose of this is to understand core data structures in python, along with 
## the primary methods used for each
## 1. list (also acts like a stack)
## 1b. common methods
## 1c. advanced filtering and methods
## 2. tuple
## 3. set
## 4. dictionary
## 5. queue (deque)
## 6. deck (queue)
## 7. string
## 8. array
## 20. linked list
## 30. tree
## 40. graph

# 1. list
## 1a. list instantiate
list_one = [1, 2, 3, 4]
print(list_one)
list_two = list((5, 6, 7, 8)) # converts tuple to list
print(list_two)
tup = (9, 10, 11, 12)
list_three = list(tup)
print(list_three)

## 1b. common methods
list_one.append(44)
print(list_one)
list_one.pop(0) # based on index - first item
print(list_one)
list_one.pop() # based on last item, default index = -1
print(list_one)
list_one.insert(2, 66)
print(list_one)
list_one.remove(2)
print(list_one)
list_one.sort()
print(list_one)
list_one.sort(reverse=True)
print(list_one)
list_one.reverse()
print(list_one)
print(list_one[1:3]) # inclusive beginning, excludes end point

## 1c. advanced filtering and data science methods, lambda functionws
my_list = [0,1,2,3,4,5,6,7,8,9,10]
subset = my_list[1:8:3] # from index 1 to 8 with every 3rd value
print(subset)
neg_subset = my_list[-5:-2]
print(neg_subset)
copy = my_list[:]
copy_reverse = my_list[::-1]

# lambda (map [class], filter [class], sorted [function], reduce [function])
squares = list(map(lambda x: x**2, my_list)) # Square each number in the list
print(squares)
evens = list(filter(lambda x: x % 2 == 0, my_list)) # Filter out only even numbers
print(evens)
# Sort a list of tuples by the second item
tuples = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

from functools import reduce
total_sum = reduce(lambda x, y: x + y, my_list)
print(total_sum)

# list_info = []
# print(dir(list_info))
# help(list_info)

# numeric value lists
list_new = [1,2,3,5,6,7,4,5,6,3,6,9,8,9,8,7,8,9,8,7,5,3,1,5,3,1,1,3,5,7,9]
print(sum(list_new))
print(min(list_new))
print(max(list_new))
print(sum(list_new) / len(list_new))
print(list_new.sort()) # sorts list, doesn't return value
print(list_new)
sort_list_new = sorted(list_new)
print(sort_list_new)
print(sorted(sort_list_new,reverse=True)) # doesn't sort the list, just returns a sorted list
print(sort_list_new)

## math
import math
print(math.prod(list_new))

## stats
import statistics
print(statistics.median(list_new))
print(statistics.mode(list_new))
print(statistics.stdev(list_new))

## alternative ways to modify and filter
numbers = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,5,6,4,2,5,3,1]

# list comprehensions (faster than lambda)
square_numbers = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
even_index_numbers = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]


# lambda - confusing on use case
square = list(map(lambda x: x**2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
even_index_elements = list(filter(lambda x: x[0] % 2 == 0, enumerate(numbers)))
print(even_index_elements)
even_index_elements = [element for index, element in even_index_elements]



print(square_numbers)
print(even_numbers)
print(even_index_numbers)
print(square)
print(even)
print(even_index_elements)