import random
y = 1
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
z = people.index("Waldo")

# Show which people sit where
print(people)

# print the location seat nr. of waldo
while y == 1:
 for x in people:
  if x == "Waldo":
   z += 1
   print("Waldo zit op stoel nr", end =" ")
   print(z)
   y +=1
 
