# dit voeg je toe om de math. te laten werken in de code
import math

# aantaal appelbomen die er zijn
bomen = 333

# aantaal appelbomen de in de zon staan
zonBomen = bomen
zonBomen /= 3

# aantaal appelbomen die in de schaduw staan
schaduwBomen = bomen
schaduwBomen *= 2/3

# hoeveel percantage de appelbomen in de schaduw produceren tegen over appelbomen die in zon staan.
schaduwBoomUitgavePer = 0.80

# hoeveel appels een appelboom in de zon produceerd
zonBoomUitgave = 146

# hoeveel appels een appelboom in de schaduw produceerd
schaduwBoomUitgave = zonBoomUitgave
schaduwBoomUitgave *= schaduwBoomUitgavePer

# hoeveel appels je uiteindelijk onvangt van de zonne bomen
zonAppelsVangst = zonBomen
zonAppelsVangst *= zonBoomUitgave

# hoeveel appels je uiteindelijk onvangt van de schaduw bomen
schaduwAppelsVangst = schaduwBomen
schaduwAppelsVangst *= schaduwBoomUitgave

# aantal eigenaren van de boomgaard
eigenaren = 4

# hoeveel appels je uiteindelijk ontvangt als je alle vangst optelt van alle bomen
algemeneVangst = schaduwAppelsVangst
algemeneVangst += zonAppelsVangst
algemeneVangst = math.floor(algemeneVangst)

# hoeveel goeie appels er opgegeten worden
gegetenAppels = 0

# hoeveel appels er verkoopbaar zijn
verkoopbareAppels = algemeneVangst
verkoopbareAppels /= eigenaren
verkoopbareAppels = math.floor(verkoopbareAppels)

# je uiteindelijk deel die je gaat verkopen
deel = verkoopbareAppels
deel -= gegetenAppels

print(deel)