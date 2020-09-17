Logi = 1
Op = 1 

while Op == 1 and Logi == 1:
 print("I'm printed using a and operator")

 cheese = input("type a, A or B, b for a answer: ")
 if cheese == "a" or cheese == "A":
  print("If you typed a or A you got this answer")
  Op += 1
 elif cheese == "b" or cheese == "B":
  print("If you typed b or B you got this answer")
  Logi += 1
 else:
  print("Please answer a or b")