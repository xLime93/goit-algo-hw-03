from datetime import datetime

def get_days_from_today(date):
    return (datetime.strptime(date, "%Y-%m-%d") - datetime.today()).days

while True:
    try:
        print(get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': ")))
        break
    except ValueError:
        print("Введено дату в невірному форматі.")
        print("Введено дату в невірному форматі.")