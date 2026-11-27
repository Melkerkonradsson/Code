tal = input("skriv in heltal separerade med mellanslag:")
lista = [int(x) for x in tal.split()]
lista = [x for x in lista if x !=0]
print("listan utan nollor:", lista)
