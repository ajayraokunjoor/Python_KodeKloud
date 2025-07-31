countries = ["USA", "Canada", "India"]
print(countries)
countries[0] = "UK"
print(countries)
print(len(countries))
print(" del countries[1]")
print(countries[-3])
print("print(countries[4])")

print("Append and Insert")
countries = ["USA", "Canada", "India"]
countries.append("Spain")
print(countries)
countries.insert(2, "Italy")
print(countries)

print("Swapping variables in a list")
countries= ["USA","Canada","India"]
print(countries)
temp = countries[0]
countries[0]=countries[1]
countries[1]=temp
print(countries)

print("swapping without a extra variable")
print(countries)
countries[0], countries[1], countries[2] = countries[1], countries[2], countries[0]
print(countries)

print("Sorting and Reversing Lists")
ages = ["56", "72", "24", "46"]
ages.sort()
print(ages)
ages.reverse()
print(ages)

print("Iterating Lists")
ages = [56, 72, 24, 46]
total = 0 
for age in ages:
    total += age
print("Total ages is = ", total)
print("Compute avearage age")
average = total / len(ages)
print("Average age in the list is", average)

print("Understanding Lists")
name = "Cheeku"
ages = [56, 72, 24, 46]
ages2 = ages 
print(ages)
print(ages2)
print("Modifying Lists and the Reference Behavior")
ages[0] = 92
print(ages)
print(ages2)
print("Creating an Independent Copy of a List")
ages3 = ages[:]
ages[1] = 100
print(ages)
print(ages2)
print(ages3)
print("Slicing Lists")
letters = ["A", "B", "C", "D", "E"]
firstTwo = letters[0:2]
print(firstTwo)
print("Slicing with Single Indices")
print(letters[1:])
print(letters[:3])
print("Using Negative Indices")
print(letters[1:-1])
print(letters[:])
copy_of_letters = letters[:]
print(copy_of_letters)
print("Slicing vs Assignment")
name = "Cheeku"
ages = [56, 72, 24, 46]
ages2 = ages
ages[0] = 92
print(ages2[0])
print("Using the del keyword with slicing")
letters = ["A", "B", "C", "D", "E"]
print(letters)
del letters[1:3]
print(letters)
print(len(letters))
del letters
print("finding in lists")
letters = ["A", "B", "C", "D", "E"]
print("B" not in letters)
print("Z" not in letters)
print(" Nested Lists 2D")
classroom = [
    ["Sam", "Max", "Joe", "Anne"],
    ["Sofie", "Lisa", "Tim", "Sasha"],
    ["Claire", "Sara", "Leo", "Kim"],
    ["Zoe", "Guy", "Anna", "Eva"],
]
student = classroom[2][1]
print(student)
print(len(classroom))
print("Nested Lists 3D")
school = [
    [
        ["Sara", "Kim", "Anne", "Eva"],
        ["Johan", "Collin", "Sam", "Alex"],
        ["Luke", "Sara", "Haley", "Jennifer"],
        ["Katy", "Mara", "Max", "Roy"],
    ],
    [
        ["Anne", "Leo", "Sasha", "Tim"],
        ["Claire", "Guy", "Eva", "Zoe"],
        ["Lisa", "Max", "Evan", "Chloe"],
        ["Brent", "Sam", "Sarah", "Anne"],
    ],
    [
        ["Maria", "Julian", "Chris", "Tom"],
        ["Zoe", "Anna", "Kim", "Leo"],
        ["Vera", "Pim", "Leo", "Guy"],
        ["Anne", "Sofie", "Max", "Joe"],
    ],
    [
        ["Sam", "Max", "Joe", "Anne"],
        ["Sofie", "Lisa", "Tim", "Sasha"],
        ["Claire", "Sara", "Leo", "Kim"],
        ["Zoe", "Guy", "Anna", "Eva"],
    ],
]
student = school[1][2][1]
print(student)  # This will output: Max