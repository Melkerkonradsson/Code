#köra ett program som läser in heltal n och därefter beräknar 1+2+3+...+n

n=int(input('skriv in ett heltal n:'))
summa = 0
k = 1 

while k <=n:
    summa += 1/k
    k = k + 1
print (f'summan blir {summa:.2f}')

#köra ett program som läser in heltal n och därefter beräknar summan 1/1 + 1/2 + 1/3 ... + 1/n


