# variablen die ik later gebruik
namen = ""
vakken = ""
laatsteWoord = ""
cutTekst = ""

naamTekst = 'De python lessen worden gegeven door Erik, Erwin en ook door Hidde'

# haalt de namen uit de teskt
# voor makkelijk leesbaarheid heb ik de spatie's, comma's en een en meegegeven
namen += naamTekst[-29:-14]
namen += naamTekst[-5:]
print(namen)

vakkenTekst = 'SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer...'

# haalt de vakken uit de teskt
# voor makkelijk leesbaarheid heb ik de spatie's, comma's en een en meegegeven
vakken += vakkenTekst[15:-20]
print(vakken)

# haalt de laatste 6 letter uit de tekst
testTekst = 'Wat is hier het laatste woord?'
laatsteWoord += testTekst[-6:]
print(laatsteWoord)

# haalt de 5e letter tot en met de 8e letter en 29e letter tot de 33e letter uit de tekst
tekst = 'Het www is onwikkeld vanaf 1989 door Tim Berners-Lee'
cutTekst += tekst[4:8]
cutTekst += tekst[28:32]
print(cutTekst)