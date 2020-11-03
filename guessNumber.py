# Dette er ein kommentar
import random

print("Hallo NAV!\n")
nummer = float(input("Skriv inn eit tall mellom 1 og 10: "))
randomnummer = (random.randint(1, 10))
if nummer == randomnummer:
	print("\nDU TRAFF! Det tilfeldige tallet var: ", randomnummer)
else:
	print("\nDu bomma! Det tilfeldige tallet var: ", randomnummer)