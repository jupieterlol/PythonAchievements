# the variables to give you multiple routes
x = 1
y = 0
hungery = 0

# start of the journey

while x == 1:
 print("Its 7.00 a.m your alarm is going of because you need to go to school.")
 print("What will you do?")
 wakeUp = input("Will you wake up, snooze your alarm or turn it off: ")
 
# if else statement to let you choose if you want to wake up or go back to sleep
 if wakeUp == "Wake Up" or wakeUp == "wake up":
  print("You turn off your alarm and get out of bed.")
  x += 1
 elif wakeUp == "snooze" or wakeUp == "snooze":
  print("You snooze your alarm and go back to sleep for a little bit.")
  y += 1
 elif wakeUp == "off" or wakeUp == "turn off":
  print("You turn off your alarm and go back to sleep.")
  y += 1
 else:
  print("option's are: wake up, snooze or turn off.")

# the wake up route
 while x == 2:
  print("----------------------------------------------------------")
  print("")
  print("You get ready to go to school")
  print("You take a quick shower and make your way down stairs for some breakfast.")
  print("You open up the fridge to see what you can make for breakfast today.")
  print("The option that you have are: grilled cheese sandwich, a omelet or cruesli.")
  breakfast = input("What will I make? : ")
  
# if else statement to see what breakfast you choose
  if breakfast == "omelet":
   print("You make a delicous omelet.")
   print("The omelet looks really good so you take a picture of it and post it on instagram.")
   print("Omelet get 42,069 likes on instagram.")
   print("You're really happy with your creation that you feel like its a waste to eat it.")
   print("So you let it stay on the table and go off to school without breakfast.")
   x += 1
   hungery += 1
  elif breakfast == "cheese" or breakfast == "sandwich" or breakfast == "grilled cheese sandwich":
   print("You start making your placing your cheese sandwich in the grilling pan with some butter.")
   print("After a few minutes of grilling you hear the cheese hit the grilling pan.")
   print("You know that your sandwich is done and place it on the plate.")
   print("You start taking a bite from it and it makes you euphoric of how well it tastes.")
   print("After finishing the sandwich you pick up your stuff and you go to school.")
   x += 1
  elif breakfast == "cruesli" or breakfast == "muesli":
   print("You take the milk out of the fridge and poor it in your bowl.")
   print("Then you grab your cruesli and poor some in the milk.")
   print("Then you start eating the cruesli with your fork.")
   print("When your done with your food you get your stuff and go school.")
   x += 1
  elif breakfast == "skip":
   print("You were not hungery and went off to school without breakfast.")
   x += 1
   hungery += 1
  else:
   print("Options: grilled cheese sandwich, omelet, cruesli or skip")


# the snooze or turn off alarm route
 while y == 1:
  print("----------------------------------------------------------")
  print("")
  print("Oh no, you have overslept and you have only 10 minutes to get ready for school.")
  print("You quickly try to get ready for school.")
  print("You forgot to shower and you kind of smell. So you try to mask it with deo.")
  print("You rush down stairs and go through the door.")
  print("Off to school")
  y += 1
  hungery += 1


 while x == 3 or y == 2:
  print("----------------------------------------------------------")
  print("")
  print("You finally arrive at school.")
  print("You hear from a far someone screaming your name.")
  name = input("What is your name? : ")
  print("You look behind you and see your chilhood friend Nicky running towards you")
  print("'Hey " + name + ", how are you this morning?!!!!' Asked Nicky")
  mood = input("I'm am doing: ")
  if mood == "good" or mood == "well":
   print("'Ah thats nice to hear' says Nicky")
   x += 1
   y += 1
  elif mood == "bad":
   print("'Ah I hope you will feel better soon' Says Nicky worried")
   print("'Here have a hug' Says Nicky")
   print("Nicky gives you a hug and I feels really great")
   print("You say thanks to Nicky")
   print("You feel alot better now")
   x += 1
   y += 1
  elif mood == "okay" or mood == "fine":
   print("'Ah thats okay' says Nicky")
   x += 1
   y += 1
  else:
   print("options are: good, bad or okay")

 while x == 4 or y == 3:
  print("----------------------------------------------------------")
  print("'Lets go inside' says Nicky")
  print("You both go inside school and to your class room waiting for the class to start")
  print("The class your in right now is math class")
  print("The class is boring as ussual so you scribble a bit on your note's")
  print("Then the math teacher starts asking you if you know the sollution to the math problem")
  print("The question is : The period of 2 sin x cos x is?"
  mathAnswer = input("The anwser is : ")
  if mathAnswer == "" or mathAnswer == "":
   print("")
  elif mathAnswer == "" or mathAnswer == "":
   print("")
  else:
   print("'That is wrong' Says the math teacher")
   print("'The answer was π' Says the teacher)
   print("You feel really embarrassed that you got it wrong")
  x += 6
  y += 5



















