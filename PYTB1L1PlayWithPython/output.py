Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is michelle Frankfort')
Mijn naam is michelle Frankfort
>>> print('Mijn naam is <michelle frankfort>')
Mijn naam is <michelle frankfort>
>>> naam = "michelle frankfort
  File "<stdin>", line 1
    naam = "michelle frankfort
                             ^
SyntaxError: EOL while scanning string literal
>>> naam = "michelle frankfort"
>>> print(naam)
michelle frankfort
>>> print(naam.upper())
MICHELLE FRANKFORT
>>> print(naam[0:2])
mi
>>> print(naam[::-1])
trofknarf ellehcim
>>> leeftijd = 22
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo michelle frankfort ben je al 22 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
23
>>> leeftijd-=1
>>> leeftijd
22
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Het is alweer 4 jaar geleden dat je 18 werd ;-)
>>> from random import randint
>>> randint(0,1000)
253
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
690
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 690
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-11 14:06:58.228786
>>> datum.strftime('%A %d %B %Y')
'Friday 11 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 11 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 11 settembre 2020'
>>>
