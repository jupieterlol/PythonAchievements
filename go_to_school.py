weekdag = "zaterdag"


if weekdag == "dinsdag" or weekdag == "vrijdag":
 print("Je moet vandaag naar school toe met de trein.")
elif weekdag == "maandag" or weekdag == "woensdag" or weekdag == "donderdag":
 print("Je hebt vandaag online les.")
elif weekdag == "zaterdag" or weekdag == "zondag":
 print("Het is weekend je hebt geen school")
 print("Dus je kunt lekker uitslapen")
else:
 print("Dit is een niet bestaande dag.")