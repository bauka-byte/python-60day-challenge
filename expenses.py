expenses = []
print("=== Калкулятор Расходов ===")
print("Вводи траты в формате: <название> <сумма>")
print("Например: еда 1500")
print("Чтобы закончить, напиши: стоп\n")

while True:
    user_input = input("> ")

    if user_input.lower() == "стоп":
        break

    try:
        name, amount = user_input.split()
        amount = int(amount)
        expenses.append({"название": name, "сумма": amount})
    except ValueError:
        print("! Ошибка: вееди название и сумму через пробел (например: такси 1200)")

print("\n=== Отчёт по тратам ===")
total = 0
for expense in expenses:
    print(f"{expense['название']}: {expense['сумма']} ₸")
    total += expense["сумма"]
    
print(f"\n💰 всего потрачено: {total} ₸")
