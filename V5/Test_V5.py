
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci']}

# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

# student['phone'] = '555-5555'
# student['name'] = 'Jane'

# del student['age']

# age = student.pop('age')

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get('phone', 'not found'))
# print(student)
# print(age)

for key, value in student.items():
    print(key, value)