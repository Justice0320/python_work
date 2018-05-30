# Chapter 2 exercises

name = "Garry"
message = "Hello " + name + ", how are the Python lessons coming along?"

print(message)

# case practice

print(name.lower())
print(name.upper())
print(name.title())

# quotation

quote = '\tAlbert Einstein once said, “A person who never made a \n\tmistake never tried anything new.”\n'
print(quote)

name = "\tAlbert Einstein"
quote = name + ' once said, “A person who never made a \n\tmistake never tried anything new.”\n'
print(quote)

name = " Garry "
print(name.rstrip() + "\n")
print(name.lstrip())
print("\n\t" + name.strip())