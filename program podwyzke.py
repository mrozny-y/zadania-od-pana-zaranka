pensje = [3800,4200,5000,5700,6800]
bank=1300
prog = 5000
koszt = 0

for pensje in pensje:
    if  pensje < prog:
        podwyzka = pensje * 0.08
    else:
        podwyzka = pensje * 0.04

    print("pesje", pensje, "podwyzka",podwyzka)
    koszt += podwyzka

print("lonczny koszt podwtzek", koszt)

if koszt <= bank:
    print("budzet wystarzcy")
else:
    print("budzet nie wystarczy")
    print("brakuje", koszt - bank, "zl")
