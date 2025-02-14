""" #Strings are for representing characters, names, words etc.
name = "Deivid"
#integer represents whole numbers
age: 14
#Floats represents decimals
wallet = 5.45
#boolean represents true or false, used in evaluations
graduated = False

def add(x,y):
    print(x+y)
#input asks the user a question and stores their response as a value
bill = float(input("what was the bill"))
#print (type(bill))
#add(40,bill)

#lists
students = ["Joanna", "Deivid", "David", "other David", "Ethan"]
#similar to saying for i in range (5): print (students[i])
print(students[4])
for student in students:
    print(student)
moneys = [1,2,3,4,5,6]
total = 0
for money in moneys:
    total = total + money
    print(total) """

""" # tip calculator
def add(x,y):
    return(x+y) # return stores the code so it can be used wherever you need it
bill = float(input("Bill: "))
tip = int(input("Tip: ")) # whole number
print (type(bill)) # This prints the type of the bill to check if it's a float
print (type(tip)) # This prints the type of the tip to check if it's an integer
total = add(bill,tip)
print(f"Total: {total}") """


""" sentence = input("Enter Sentence: ") # asks user for input

def count_words(sentence): # takes the sentence as input
    words = sentence.split() # splits up words in the sentence
    return len(words) # Return the number of words by using len() to count the list length

print("Number of words: ", count_words(sentence)) # calls on the code """


# mad libs project
""" verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter another verb: ")
noun = input("Enter a noun: ")
number = input("Enter a number: ")
celebrity1 = input("Enter a celebrity name: ")
celeb2 = input("Enter another celebrity name: ")
celeb3 = input("Enter another celebrity name: ")
adjective = input("Enter an adjective: ")

Madlib = f"It was a {adjective} day in Staten Island Technical Highschool. As {celebrity1} walked into {number} period, he suddenly started {verb1} because he saw {celeb2}. {celeb2} was so shocked that he started {verb2}. Then, the teacher, {celeb3}, walked in and {verb3} at everyone to sit down. A new day at Staten Island Tech has started."

print(Madlib) """


# challenge 1
# number = blank
# if number = even
# print('even')
# else:
# print('odd')
""" number = int(input("Enter Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("odd") """

# challenge 2
""" bill = float(input("Bill Amount: "))
service = int(input("Please Rate Service Out of 5: "))
bad = 0
okay = 15
good = 20
great = 25
okay_tip = (okay / 100) * bill
good_tip = (good / 100) * bill
great_tip = (great / 100) * bill
if service >= 5:
    print(great_tip + bill)
elif service == 4:
    print(good_tip)
elif service == 3: 
    print(okay_tip)
else:
    print(bill) """

# challenge 3
""" factors = []
number = int(input("Enter Number: "))
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print(factors) """

# challenge 4
""" factors1 = []
factors2 = []
number1 = int(input("Enter Number: "))
number2 = int(input("Enter Another Number: "))
for i in range(1, number1 + 1):
    if number1 % i == 0: # you can write "and if number2 %..." to combine the for loops
        factors1.append(i)
for j in range(1, number2 + 1):
    if number2 % j == 0:
        factors2.append(j)
commons = []
for factor in factors1:
    if factor in factors2:
        commons.append(factor)
all_commons = len(commons)
print(f"Greatest Common Factor: {commons[all_commons - 1]}")  """
