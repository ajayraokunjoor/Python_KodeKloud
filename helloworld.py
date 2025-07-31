print("hello world!")
print ("Hello! \"Python\" is cool")
print('Hello! "Python" is cool')
print("Hello! 'Python' is cool")
print(2 ** 3)    # 8
print(2. ** 3.)  # 8.0
print(2 ** 3.)   # 8.0
print(2. ** 3)   # 8.0
print(2 * 3)     # 6
print(2. * 3.)   # 6.0
print(2 * 3.)    # 6.0
print(2. * 3)    # 6.0
print(10 / 2)    # 5.0
print(10. / 2.)  # 5.0
print(10. / 2)   # 5.0
print(4 % 2)     # 0
print(5 % 2)     #1 
print(-6 - 6)   # -12
print(10 - -6)  # 16
print(10 - 6 ** 2 / 9 * 10 + 1)
print(2 * (2 + 3))  # 10
print(2 * 5)
# Output: 


# Defining the variables with contextual names
amount_of_apples = 2
cost_of_apple = 5


# Calculating the total cost using the defined variables
print(amount_of_apples * cost_of_apple)
# Output: 10


# Updating the variable to reflect a price increase
cost_of_apple = cost_of_apple + 2
print(amount_of_apples * cost_of_apple)
# With updated cost_of_apple = 7, the output is: 14

# Using the '+=' operator for a more concise update
cost_of_apple += 2
print(amount_of_apples * cost_of_apple)
# Output: 14

amount_of_apples = 2
cost_of_apple = 5
print(amount_of_apples * cost_of_apple)

input("How are you feeling today? ")

favorite_color = input("What is your favorite color? ")
print("Your favorite color is " + favorite_color)

cost_of_apple = 2
amount_of_apples = input("How many apples do you want? ")  # User might input: 10
total_sum = cost_of_apple * int(amount_of_apples)
print("The total cost is: " + str(total_sum))
