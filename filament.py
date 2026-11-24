filament=[150,240,175,260,195,310,225,180,275,160]
ile = 0
suma = 0
for i in range(0,len(filament)):
    if filament[i] > 220:
        ile+=1
        suma = suma + filament[i]
print("filamentow ktore majom wiencej niz 220 jest",ile)
print("cale zuzycie filamentow ktore majom wiencej niz 220 jest",suma)
if ile > 4:
    print("opiekun musi spawdzic co jest  nie tak")
else:
    print("wszystko jest dobrze")
