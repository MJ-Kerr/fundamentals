num1 = 42 #declares num1 is equal to 42
num2 = 2.3 #declares num2 is equal to 2.3
boolean = True #declares boolean is equal to True
string = 'Hello World' #declares string is equal to 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declares pizza_toppings is equal to ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declares person is equal to {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana') #declares fruit is equal to ('blueberry', 'strawberry', 'banana')
print(type(fruit)) #prints the type of fruit
print(pizza_toppings[1]) #prints the value of pizza_toppings[1]
pizza_toppings.append('Mushrooms') #adds the value of pizza_toppings[1] to pizza_toppings
print(person['name']) #prints the value of person['name']
person['name'] = 'George' #sets the value of person['name'] to 'George'
person['eye_color'] = 'blue' #sets the value of person['eye_color'] to 'blue'
print(fruit[2]) #prints the value of fruit[2]

if num1 > 45: #checks if num1 is greater than 45
    print("It's greater") #prints "It's greater"
else: #checks if num1 is less than 45
    print("It's lower") #prints "It's lower"

if len(string) < 5: #checks if string length is less than 5
    print("It's a short word!") #prints "It's a short word!"
elif len(string) > 15: #checks if string length is greater than 15
    print("It's a long word!") #prints "It's a long word!"
else: #checks if string length is equal to 15
    print("Just right!") #prints "Just right!"

for x in range(5): #loops through 5 times
    print(x) #prints 0, 1, 2, 3, 4
for x in range(2,5): #loops through 2 to 5 times
    print(x) #prints 2, 3, 4, 5
for x in range(2,10,3): #loops through 2 to 10 times and 3 times
    print(x) #prints 2, 5, 8, 11, 14, 
x = 0 #declares x is equal to 0
while(x < 5): #while loop
    print(x) #prints 0, 1, 2, 3, 4
    x += 1 #increments x by 1

pizza_toppings.pop() #removes the last value of pizza_toppings
pizza_toppings.pop(1) #removes the value of pizza_toppings[1]

print(person) #prints the value of person
person.pop('eye_color') #removes the value of person['eye_color']
print(person) #prints the value of person

for topping in pizza_toppings: #loops through pizza_toppings
    if topping == 'Pepperoni': #checks if topping is equal to 'Pepperoni'
        continue #skips the rest of the for loop
    print('After 1st if statement') #prints 'After 1st if statement'
    if topping == 'Olives': #checks if topping is equal to 'Olives'
        break #breaks the rest of the for loop

def print_hello_ten_times(): #prints hello ten times
    for num in range(10): #loops through 10 times
        print('Hello') #prints 'Hello'

print_hello_ten_times() #prints hello ten times

def print_hello_x_times(x): #prints hello x times
    for num in range(x): #loops through x times
        print('Hello') #prints 'Hello'

print_hello_x_times(4) #prints hello 4 times

def print_hello_x_or_ten_times(x = 10): #prints hello x or 10 times
    for num in range(x): #loops through x times
        print('Hello') #prints 'Hello'

print_hello_x_or_ten_times() #prints hello x or 10 times
print_hello_x_or_ten_times(4) #prints hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)