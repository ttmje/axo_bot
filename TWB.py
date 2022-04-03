import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime
import keyboard

x1 = input("Введите координаты x1: ")
try:
    x1 = int(x1)
    print("x1 = : ", x1)
except ValueError:
    x1 = 1340
    print("Ставлю x1 по умолчанию для FULL HD монитора:", x1)

y1 = input("Введите координаты y1: ")
try:
    y1 = int(y1)
    print("y1 = : ", y1)
except ValueError:
    y1 = 345
    print("Ставлю y1 по умолчанию для FULL HD монитора:", y1)

x2 = input("Введите координаты x2: ")
try:
    x2 = int(x2)
    print("x2 = : ", x2)
except ValueError:
    x2 = 1303
    print("Ставлю x2 по умолчанию для FULL HD монитора:", x2)

y2 = input("Введите координаты y2: ")
try:
    y2 = int(y2)
    print("y2 = : ", y2)
except ValueError:
    y2 = 495
    print("Ставлю y2 по умолчанию для FULL HD монитора:", y2)


def TWBf():
    monitor3 = {
            "left": x1, # координаты кнопки CLAIM NOW
            "top": y1,
            "width": 35, # размер
            "height": 25,
    }
    monitor4 = {
        "left": x2,
        "top": y2,
        "width": 3,  # размер
        "height": 3,
    }

    def find_color3(our_color3, monitor3={}):
        # проба цвета с координат
        m3 = mss()
        # получаем пиксель с монитора
        img3 = m3.grab(monitor3)
        # преобразуем пиксель в матрицу
        img_arr3 = np.array(img3)
        # поиск цвета (b, g, r alpha)
        our_map3 = (our_color3[2],our_color3[1],our_color3[0],255)
        indexes3 = np.where(np.all(img_arr3 == our_map3, axis=-1))
        our_crd3 = np.transpose(indexes3)
        return our_crd3

    def find_color4(our_color4, monitor4={}):
        # проба цвета с координат
        m4 = mss()
        # получаем пиксель с монитора
        img4 = m4.grab(monitor4)
        # преобразуем пиксель в матрицу
        img_arr4 = np.array(img4)
        # поиск цвета (b, g, r alpha)
        our_map4 = (our_color4[2], our_color4[1], our_color4[0], 255)
        indexes4 = np.where(np.all(img_arr4 == our_map4, axis=-1))
        our_crd4 = np.transpose(indexes4)
        return our_crd4

    our_color3 = [255,13,95]     # КРАСНЫЙ цвет с кнопки
    our_color4 = [234, 234, 234] # Серый цвет АНТИКАПЧИ
    while True:
        time1 = time.time()
        result = find_color3(our_color3, monitor3)
        result2 = find_color4(our_color4, monitor4)
        time2 = time.time()
        if result2.__len__():
            keyboard.press("F5")
            time.sleep(2)
            print('Нажал кнопку Refresh:', datetime.datetime.now())
        if result.__len__():
            x = result[0][1] + monitor3.get("left")
            y = result[0][0] + monitor3.get("top")
            pg.moveTo(x+59, y+11)  # перемещение мыши по координатам где найден цвет
            pg.click(x+59, y+11, interval=1)  # клик
            time.sleep(3)
            pg.moveTo(x + 200, y - 200)
