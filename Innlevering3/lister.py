import math
#Oppgave 1
liste1 = [5, 17, 23, 22]
print(liste1[1:3])

#Oppgave 2
liste2 = []
for i in range(4):
    input2 = input("Skriv et et navn: ")
    liste2.append(input2)

#Oppgave 3
if "Celine" in liste2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Oppgave 4
sumListe = sum(liste1)
produktListe = math.prod(liste1)
print(f"Summen av listen er {sumListe}")
print(f"Produktet av listen er {produktListe}")
liste3 = [sumListe, produktListe]
liste4 = liste1 + liste3
print(liste4)
for i in range(2):
    liste4.pop()
    print(liste4)