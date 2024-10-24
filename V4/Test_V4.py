# Lists

# courses = ['History', 'Math', 'Physics', 'ComSci']
# courses_2 = ['Art', 'Education']
# nums = [1, 5, 2, 4, 3]

# append() is a method to add an item to the end of a list
# courses.append('Art')

# insert() is a method to add an item to a certain index of a list
# courses.insert(0, 'Art')

# extend() is a method to add contant of a list to another list
# courses.extend(courses_2)

# remove() is a method to remove a certain item from a list
# courses.remove('Math')

# pop() is a method to remove the last item from a list [It retuns the removed item]
# popped = courses.pop()

# reverse() is a method to reverse a list
# courses.reverse()

# sort() is a method to sort a list
# [If the items are words or characters it will be sorted alphabatiaclly
#  if the items are numbers it will be sorted in ascending order]
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted() is a function that returns a sorted list
# sorted_courses = sorted(courses)

# min() is a function that returns the minimum number in a list
# min_num = min(nums)

# max() is a function that returns the maximum number in a list
# max_num = max(nums)

# sum() is a function that returns the sumition of numbers in a list
# sum_num = sum(nums)

# index() is a method to find the index of a certain item
# inx = courses.index('ComSci')

# in is an operator that checks if there is a certain item in a list or not [Returns True or False]
# value = 'Art' in courses

# enumerate() is a function that returns the index of an item and its value
# for loop to print each item in a list
# start makes the print printing from a certain index without changing the value of the item
# for index, course in enumerate(courses, start=1):
#     print(index, course)

# join() is a method used to turn list into a string
# split() is a method to turn string into a list
# course_str = ' - '.join(courses)
# new_list = course_str.split(' - ')

# print(courses)
# print(nums)
# print(sorted_courses)
# print(popped)
# print(min_num)
# print(max_num)
# print(sum_num)
# print(inx)
# print(value)
# print(course_str)
# print(new_list)







# Mutable
# list_1 = ['History', 'Math', 'Physics', 'ComSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'ComSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)







# Sets

# cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'}
# art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}

# intersection() is a method that shows the common items between sets
# difference() is a method that shows the different items between sets
# union() is a mehtod to combine sets together

# print(cs_courses)
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))







# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()