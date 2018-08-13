# 4-10 Slices

my_foods = ['pizza', 'falafel', 'carrot cake', 'burger', 'chips', 'curry', 'chili']

my_foods.append('cannoli')

print("My favourite foods are:")
print(my_foods)

print("\nThe first three items in the list are:")
print(my_foods[:3])

print("\nThe items from the middle of the list are:")
print(my_foods[2:5])

print("\nThe last three items in the list are:")
print(my_foods[-3:])

# 4-11 My Pizzas, You Pizzas

pizzas = ['pepperoni', 'cheese', 'mexican']
friend_pizzas = pizzas[:]

friend_pizzas.append('ham and pineapple')

for pizza in pizzas:
    print('My favourite flavour of pizzas are, ' + pizza + '!\n')

for fpizza in friend_pizzas:
    print("My friend's favourite flavours of pizza are, " + fpizza + '!\n')

# 4-12 More Loops

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favourite foods are:")
for ffood in friend_foods:
    print(ffood)
