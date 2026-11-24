co2 = [750,990,1100,880,1240,1180,1050,820,1300,970]
ilosc = 0
razem = 0
prog = 1200
for i in co2:
    if i > prog:
        razem+=i-prog
        ilosc+=1

    
print(f"tyle jest ilosci wnyikow wiencej niz {prog} jest ich {ilosc}")  
print(razem)

if ilosc > 3:
    print("TAK")
else:
    print("NIE")
