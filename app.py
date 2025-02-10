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


""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """


""" sentence = input("Enter Sentence: ") # asks user for input

def count_words(sentence): # takes the sentence as input
    words = sentence.split() # splits up words in the sentence
    return len(words) # Return the number of words by using len() to count the list length

print("Number of words: ", count_words(sentence)) # calls on the code """


# mad libs project
""" verb1 = "crying"
verb2 = "throwing up"
verb3 = "drank"
noun = "sunfish"
number = "fifth"
celebrity1 = "Kendrick Lamar"
celeb2 = "Drake"
celeb3 = "Beyonce"
adjective = "new" """

verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter another verb: ")
noun = input("Enter a noun: ")
number = input("Enter a number: ")
celebrity1 = input("Enter a celebrity name: ")
celeb2 = input("Enter another celebrity name: ")
celeb3 = input("Enter another celebrity name: ")
adjective = input("Enter an adjective: ")

Madlib = f"It was a {adjective} day in Staten Island Technical Highschool. As {celebrity1} walked into {number} period, he suddenly started {verb1} because he saw {celeb2}. {celeb2} was so shocked that he started {verb2}. Then, the teacher, {celeb3}, walked in and {verb3} at everyone to sit down. A new day at Staten Island Tech has started."

print(Madlib)