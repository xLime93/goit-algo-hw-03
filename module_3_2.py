import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    else:
        return sorted(random.sample(range(min,max + 1), quantity))

while True:
    try:
        print(get_numbers_ticket(int(input('Введіть мінімальне можливе число у наборі (не менше 1): ')), 
                                int(input('Введіть максимальне можливе число у наборі (не більше 1000): ')), 
                                int(input('Введіть кількість чисел, які потрібно вибрати: '))))
    except ValueError:
        print('Отримано невірний тип даних!')