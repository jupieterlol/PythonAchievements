print("Hallo nieuwe gebruiker wat is u naam?")
gebruiker = input("Mijn naam is :")
print("Oh hallo " + gebruiker + ". Hoe oud ben je?")
leeftijd = input("Mijn leeftijd is:")
print("Zo je bent " + leeftijd + " jaar oud.")

# check of je jonger dan 18 bent of ouder dan 50 jaar oud
if float(leeftijd) <= 17:
 print("Dat is best jong.")
elif float(leeftijd) >= 50:
 print("Dat is een fantastische leeftijd.")
else:
 print("Dat is een mooie leeftijd.")

print("Waar kom je vandaan, " + gebruiker + "?")
plek = input("Ik kom uit: ")
print("Oke, zo jij komt uit " + plek + ".")

print("Dankje wel, " + gebruiker + ".")
print("Hoop je snel weer te ontmoeten want het is hier best eenzaam.") 