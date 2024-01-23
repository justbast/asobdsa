DVD = 890
Videogame = 890

if DVD > Videogame :
  print("DVD is more expensive than Videogame")
elif DVD < Videogame:
  print("Videogame is more expensive than DVD")
else:
  print("DVD and Videogame are the same price")

#number1 = float(input("Zadejte první číslo: "))
#number2 = float(input("Zadejte druhé  číslo: "))
#operace = input("Zadejte operaci *,-,/,+")

#def my_function (number1, number2, operace, vysledek): 
  #if operace == "*":
   # number1 * number2 = vysledek
    #print(vysledek)
 # elif operace == "+":
  #  number1 + number2 = vysledek


nakupnilist = ["Jabka", "vajca", "strouhanka", "zelí", "mléko"]
print(nakupnilist[1])
print(len(nakupnilist))
nakupnilist.insert(3, "meloun")
print(len(nakupnilist))
print(nakupnilist)
if "vajca" in nakupnilist:
  print("Vajca tam jsou")