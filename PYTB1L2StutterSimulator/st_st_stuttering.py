# the sentence you want to let the pc stutter over
sentence = input()

# set the input into a list
myList = sentence.split()

# cuts of the first two letters of the word
a = slice(2)

# the var where our sentence is going to go
st_st_stutter = ""

# check if the word in the list is longer than 2 letters
# if it is add stutter effect to the word
# if not just send back the word normally
for x in myList:
 if len(x) > 2:
  st_st_stutter += x[a] + "... " + x[a] + "... " + x + " "
 else:
  st_st_stutter += x + " "

# prints our sentence with stutter effect
print(st_st_stutter)