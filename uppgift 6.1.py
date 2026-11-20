antal = int(input("Hur många tal ska följden innehålla? "))
talfojld  = []
tal = 2
for i in range(antal):
    talfojld.append(tal)
    tal = tal * 3 
print (talfojld)