import random #hämtar funktioner för att skapa slumptal
tal = [random.randint(1, 1000) for i in range(100)] 
minsta = min(tal)
största = max (tal)
medelvärde = sum(tal) / len(tal)
print("minsta talet:", minsta)
print("största talet:", största)
print("medelvärdet:", medelvärde)