print ("Dans supermarket")

while True:
    numbers = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 0.5:0}
    #INPUT + Basic calculation
    command=input("Indtast totalprisen: ")
    if command.isnumeric()==False:
        break

    item_cost = float(command)
    moneygiven = float(input("Indtast hvor mange penge du modtog: "))
    moneyback = moneygiven - item_cost
    if moneygiven < item_cost:
        print ("ERROR")
        break

    print ("Du skal give", moneyback, "tilbage")
    for i, j in numbers.items():
        numbers[i] = moneyback // i
        moneyback -= numbers[i] * i
        print (int(numbers[i]), " x ", i, "kroner")


