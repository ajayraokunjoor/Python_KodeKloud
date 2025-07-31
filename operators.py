age1 = 24
age2 = 16


if age1 >= 18 and age2 >= 18:
    print("You are both adults")
elif age1 >= 18 or age2 >= 18:
    print("One of you is an adult")
else:
    print("You are both children")

is_hungry = False
if not is_hungry:
    print("You are not hungry")
    print(15 | 22)
    print(15 & 22)
    print(15 ^ 22)
    print(~15)
    print(22 >> 2)

    # Arithmetic operations
print(22 // 2)
print(22 // 4)
print(22 * 2)
print(22 * 4)

# Corresponding bit shifts
print(22 >> 1)
print(22 >> 2)
print(22 << 1)
print(22 << 2)