def goToStore():
 print("It's smart to get food from the store")
def goOrderOut():
 print("You can afford to order food")
def notHungery():
 print("Not hungery right now")
# how hungery you are
hunger = 45
# time last eaten in min
timeLastEaten = 350
# money in cents
money = 2000
weekend = True
canMissMoney = True
# do you want to cook
cook = False
if timeLastEaten > 599:
 canWaitForFood = False
else:
 canWaitForFood = True
 

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