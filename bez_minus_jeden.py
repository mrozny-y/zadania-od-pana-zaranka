slowa = []

for i in range(5):
    wpisane = input("Podaj słowo: ")
    slowa.append(wpisane)
 

    for slowo in slowa:
    odwrocone = "".join(reversed(slowo))
    if slowo == odwrocone:
        print(f"Palindromem jest -> {slowo}")
