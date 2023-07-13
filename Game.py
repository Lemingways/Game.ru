field = [[" "] * 3 for i in range(3)]
count = 0
print(" Добро пожаловать ")
print("      в игру      ")
print('"Крестики - Нолики"')
print("-" * 19)
print(" Формат ввода:x, y")
print(" x - номер строки")
print(" y - номер столбца")
print("-" * 19)
print("   Хорошей игры! ")
print()
print()


def show():
    print("  | 0 | 1 | 2 |")
    for i in range(3):
        row = " | ".join(field[i])
        print(f"{i} | {row} |")
        print("_______________")


def ask():
    while True:
        if count % 2 == 0:
            print(" Ходит нолик!")
        else:
            print(" Ходит крестик!")

        courds = input("       Ваш ход:").split()

        if len(courds) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = courds

        if not x.isdigit() and not y.isdigit():
            print(" Введите число! ")
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print(" Позиция занята! ")

        else:
            print(" Выход за рамки поля! ")


def winn_chek():
    win_comb = [((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for comb in win_comb:
        symbols = []
        for c in comb:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("  Выиграл X! ")
            return True
        if symbols == ["0", "0", "0"]:
            print("  Выиграл 0! ")
            return True
    return False



while True:
    count += 1
    show()
    x, y = ask()
    if count % 2 == 0:
        field[x][y] = "0"
    else:
        field[x][y] = "X"
    a = winn_chek()
    if a:
        show()
        break
    if count == 9:
        print("Ничья")
        show()
        break