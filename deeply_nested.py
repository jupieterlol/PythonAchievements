# functions
def goToStore():
 print("It's smart to get food from the store.")
def goOrderOut():
 print("You can afford to order food.")
def notHungery():
 print("Not hungery right now.")

# how hungery you are
hunger = 45

# time last eaten in min
timeLastEaten = 350

# money in cents
money = 2000

# is it weekend
weekend = True

# can you miss money at the moment
canMissMoney = True

# do you want to cook
cook = False

# will you have vistors over soon
vistorsSoon = False

# do you need to do something soon.
noTime = False

#check if you can wait for food
if timeLastEaten > 599 or vistorsSoon == True or noTime == True:
 canWaitForFood = False
else:
 canWaitForFood = True
 
# check if you need food and if you can afford to order out.
if hunger > 50 or timeLastEaten > 300:
 if weekend or canMissMoney:
  if money >= 2000:
   if cook == False:   
    if canWaitForFood:
     goOrderOut()
    else:
     goToStore()
   else:
    goToStore()
else:
 notHungery()