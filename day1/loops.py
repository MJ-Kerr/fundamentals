
students = ['Alex', 'Martha', 'Roger', 'Julie']

# prints the whole list
for i in range(len(students)):
    print (students[i])
print("----")

for i in range(10):
    print(i)
print("----")

for i in range (2,5):
    print(i)
print("----")

for i in range(2,20,3):
    print(i)
print("----")

# Print the students list backwards
for i in range(len(students) - 1, -1, -1):
    print (students[i])
print("----")

for element in students:
    print(element)
print("----")

index = 0
for name in students:
    print(name)
    print(index)
    index += 1

    