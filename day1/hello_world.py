# 1. TASK: print "Hello World"
print('Hello Noelle!')
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print('Hello', name, '!')  # with a comma
print('Hello ' + name + '!')  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print('Hello', name, '!')  # with a comma
# print('Hello' + name + '!')  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2} .")  # with an f string

drawers = ["documents", "envelopes", "pens"]

# access the drawer with index of 0 and print value
print(drawers[0])  # prints documents
# access the drawer with index of 1 and print value
print(drawers[1])  # prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2])  # prints pens

# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers)  # prints ["tchotchkes", "envelopes", "pens"]

# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]

# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers)  # prints ["tchotchkes", "tchotchkes", "pens"]
