
# Strings are immutable

# a = 'corey'
# print(a)
# print('Address of a is {}'.format(id(a)))

# Being immutable does not mean you can not asign the same variable to a different value

# a = 'john'
# print(a)
# print('Addressof a is {}'.format(id(a)))

# a[0] = 'C'



# Lists are mutable

a = [1, 2, 3, 4, 5]
print(a)
print('Address of a is {}'.format(id(a)))

a[0] = 6
print(a)
print('Address of a is {}'.format(id(a)))