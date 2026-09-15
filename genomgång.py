ålder = int(input("hur gammal är du"))

if ålder == 17:
    print("du är lika gammal som de flästa i ee25")

if ålder != 43:
    print("du är inte lika gammal som per")
else:
    print("du är lika gammal som per")

if ålder <= 13:
    print("du är väldigt ung")
elif ålder < 18:
    print("du får inte ta körkort")
elif ålder < 20:
    print("du får ta körkort")
else:
    print("du får handla på systembolaget")
    
    
    namn= input("Vad heter du?")
    if namn == per:
        print("kung")
    else:
        print("så stavar man inte")