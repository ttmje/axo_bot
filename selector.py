import time
from datetime import datetime
import keyboard
# задаем время сна на окне
sleep = input("Введите ВРЕМЯ переключения столов (по умолчанию 16): ")
try:
    sleep = int(sleep)
    print("Время переключения: ", sleep)
except ValueError:
    sleep = 16
    print("Ставлю колличество по умолчанию:", sleep)

# задать количество столов
st1 = input("Введите колличество столов, кратно 4 (по умолчанию 24): ")
try:
    st1 = int(st1)
    print("Колличество столов: ", st1)
except ValueError:
    st1 = 24
    print("Ставлю колличество по умолчанию:", st1)
#кнопки
next = "Ctrl + windows + right"
prev = "Ctrl + windows + left"
def group1(st1, sleep):
    while True:
                time.sleep(sleep)
                for i in range(st1):
                        keyboard.press_and_release(next)
                        print("Переключил на следующий стол в группе: ", datetime.now().strftime("%d/%m/%y %I:%M:%S"))
                        time.sleep(sleep)
                else:
                    for i in range(st1):
                        keyboard.press_and_release(prev)
                    print("ЗАКОНЧИЛ ЦИКЛ И ВЕРНУЛСЯ НА САМОЕ ПЕРВОЕ ОКНО")

