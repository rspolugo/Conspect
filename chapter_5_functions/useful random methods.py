from random import * # gives all methods of the random module without random word
# shuffle - shuffle the numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(numbers)
print(numbers)

# choice - gives random numbers or text
print(choice(numbers))
x = 'foobag'
print(choice(x))

# sample - returns amount numbers or symbols
print(sample(x, 4))

