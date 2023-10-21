salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
moneyCapital = int(0)


for i in range(10):
    moneyCapital = moneyCapital + salary - spend
    spend = spend + spend * increase
moneyCapital = int(moneyCapital) * (-1)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", moneyCapital)
