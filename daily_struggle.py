# the variables to give you multiple routes
x = 1
y = 0
hungery = 0

# start of the journey

while x == 1:
 print("Its 7.00 a.m your alarm is going of because you need to go to school.")
 print("What will you do?")
 wakeUp = input("Will you wake up, snooze your alarm or turn it off: ")
 print("----------------------------------------------------------")
 print("")

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
  print("You get ready to go to school")
  print("You take a quick shower and make your way down stairs for some breakfast.")
  print("You open up the fridge to see what you can make for breakfast today.")
  print("The option that you have are: grilled cheese sandwich, a omelet or cruesli.")
  breakfast = input("What will I make? : ")
  print("----------------------------------------------------------")
  print("")

# what happens when you choose breakfast
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
  print("Oh no, you have overslept and you have only 10 minutes to get ready for school.")
  print("You quickly try to get ready for school.")
  print("You forgot to shower and you kind of smell. So you try to mask it with deo.")
  print("You rush down stairs and go through the door.")
  print("Off to school")
  y += 1
  hungery += 1

#childhoodfriend part
 while x == 3 or y == 2:
  print("You finally arrive at school.")
  print("You hear from a far someone screaming your name.")
  name = input("What is your name? : ")
  print("----------------------------------------------------------")
  print("")
  print("You look behind you and see your chilhood friend Nicky running towards you")
  print("'Hey " + name + ", how are you this morning?!!!!' Asked Nicky")
  mood = input("I'm am doing: ")
  print("----------------------------------------------------------")
  print("")
  
# give the right responds to your mood
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

# math teacher part
 while x == 4 or y == 3:
  print("'Lets go inside' says Nicky")
  print("You both go inside school and to your class room waiting for the class to start")
  print("The class your in right now is math class")
  print("The class is boring as ussual so you scribble a bit on your note's")
  print("Then the math teacher starts asking you if you know the sollution to the math problem")
  print("The question is : The period of 2 sin x cos x is?")
  mathAnswer = input("The anwser is: ")
  print("----------------------------------------------------------")
  print(" ")

# reaction to the answer given
  if mathAnswer == "π" or mathAnswer == "pi" or mathAnswer == "Pi" :
   print("'Indeed the answer is pi (π)' Says the teacher.")
   print("'I almost though your were not paying any attation to the class well done' Says the teacher proudly.")
   print("You are extremely proud of yourself for knowing the answer to the question.")
   print("Because you never pay attantion in math class and suck at math.")
   x += 1
   y += 1
  elif mathAnswer == "phi" or mathAnser == "Phi":
   print("'Close, but the anwer I was looking for is pi (π) and not phi (φ)' Says the teacher.")
   print("The class starts burtsting out in laughter.")
   print("You feel really bad for giving the bad answer and almost start crying.")
   print("Lucky stands Nicky up for you and says 'You shouldn't laugh you could have made the same mistake'")
   print("The whole class is suddely silent.")
   print("Then says the teacher 'Yeah thats right Nicky. But lets continue the lesson.'")
   print("You were greatfull that Nicky was there for you.")
   x += 1
   y += 1
  else:
   print("'That is wrong' Says the math teacher.")
   print("'The answer was π' Says the teacher.")
   print("You feel really embarrassed that you got it wrong.")
   x += 1
   y += 1

#lunchbreak
while x == 5 or y == 4:
 print("The class continuous for quite a while until the school bell rings.")

# check if you have eaten or not. 
 if y == 4:
  print("Because you rushed out of the house early you didn't had time to eat")
  print("Lets go to the cafeteria and get some food")
 elif hungery == 1:
  print("Your stomach start to growl because you haven't eaten yet")
 else:
  print("Ah lunch break a nice time to just chill you think to yourself.")
  print("And maybe to also grab some lunch.")

# continue lunchbreak
 print("You go together with Nicky to the cafeteria to chill and get some food.")
 print("You go to the lunchlady to order some food.")
 print("They have today on the menu: cheese sandwich, omelet and a toastie.")
 foodChoose = input("I want a: ")
 print("----------------------------------------------------------")
 print("")

# foodchoose 
 if foodChoose == "cheese" or foodChoose == "sandwich" or foodChoose == "cheese sandwich":
  print("You choose the cheese sandwich.")
 elif foodChoose == "omelet" or foodChoose == "Omelet":
  print("You choose to get a omelet.")
  print("The omelet looks pretty nice.")
  print("You take a bite out of it.")
  print("Your face lights up of pure joy.")
  print("After finishing the omelet you get ready to go back to class.")
 elif foodChoose == "" or foodChoose == "":
  print("")
 elif foodChoose == "skip" and hungery == 0:
  print("You didn't feel like ordering food because you had this morning a pretty great meal.")
  print("Nicky sees this and asks 'Are you not hungery?'")
  print("You say no because you had " + breakfast + " as breakfast.")
  print("Nicky says 'Okay lets find a place to sit.'")
  print("You have a chat with Nicky about alot of things including cute guys and girls")
  print("After done talking you grab your stuff to go back to class.")
 elif foodChoose == "skip" and hungery == 1:
  print("That is not a smart choose because you haven't eaten yet.")
  print("Your Nicky sees that you want to skip lunch will you look really hungery.")
  print("So Nicky gives you a part of her lunch.")
  print("You get a penaut butter and jelly sandwich.")
  print("Its your favorite type of sandwich.")
  print("You say thank you to Nicky and eat the sandwich.")
  print("After eating the sandwich you grab your stuff to go back to class.")
 else:
  print("") 
 x += 6
 y += 5



















