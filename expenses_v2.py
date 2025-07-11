import json
import os

FILENAME = "data.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME,"r", encoding="utf-8") as f:
            return json.load(f)
    return {}
    
def save_expenses(expenses):
        with open(FILENAME, "w", encoding="utf-8")as f:
            json.dump(expenses, f, indent=2, ensure_ascii=False)

def main():
     print("=== Калькулятор Расходов v2 ===")
     expenses = load_expenses()

     while True:
          user_input = input("> ")

          if user_input.lower() =="стоп":
            break
          
          try:
              name, amount = user_input.split()
              amount = int(amount)
              expenses[name] = expenses.get(name,0) + amount
          except:
              print("⚠️ Ошибка: введи название и сумму через пробел (например: кофе 500)")

     save_expenses(expenses)

     print("\n=== Отчёт по тратам ===")
     total = 0                                                                          
     for name, amount in expenses.items():
         print(f"{name}: {amount} ₸")
         total += amount
         print(f"\n💰 Всего потрачено: {total} ")

if __name__ == "__main__":
    main()