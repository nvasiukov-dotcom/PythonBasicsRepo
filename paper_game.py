from random import choice
User: str = input("Выберите один из вариантов, Камень или Ножницы или Бумага: ")
Comp: str = choice(["Камень", "Ножницы", "Бумага"])
print("Выбор игрока: ",(User))
print("Выбор компютера: ",(Comp))
if User == Comp:
    print("Ничья")
elif User == "Камень":
    if Comp == "Ножницы":
        print("Вы победили")
    else:
        print("Вы проиграли")
elif User == "Ножницы":
    if Comp == "Бумага":
        print("Вы победили")
    else:
        print("Вы проиграли")
elif User == "Бумага":
    if Comp == "Камень":
         print("Вы победили")
    else:
        print("Вы проиграли")

            
            
