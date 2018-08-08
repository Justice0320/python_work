squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# List Comprehensions
# This lets you write the same code in a single line

squares_comp = [values ** 2 for values in range(1, 11)]
print(squares_comp)
