antal_negativa = 0 
antal = int(input("hur många tal vill du mata in"))
for i in range(antal):
    tal = int(input("skriv in ett helttal:"))
    
    if tal < 0: 
        antal_negativa += 1 
print("antal negativa tal:", antal_negativa)