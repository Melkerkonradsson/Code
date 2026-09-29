#skriva ett proramm som beräknar hur många gånger en boll studsar innan den blir still
# bollen förlorar 30% av sin höjd varje gång den studsar.

höjd=float(input('hur högt släpptes bollen ifrån i hela metrar:'))

studsar=0

while höjd >= 0.01:
    höjd=höjd*0,7
    studsar+=1

print (studsar)
