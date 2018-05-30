# Naming lesson
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)


# String whitespace
print("Python")

print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespace
favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())

print(favorite_language)

# store variable back into variable name after performing .rstrip to make change permanent
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# use .rstrip to remove right spaces, .lstrip for left spaces and .strip for both left and right spaces

