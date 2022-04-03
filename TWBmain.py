import TWB, selector
from threading import Thread
from datetime import datetime

now = datetime.now().strftime("%d/%m/%y %I:%M:%S")
print("Начало работы бота: ", now)

if __name__ == '__main__':
    TWBm = Thread(target=TWB.TWBf, args=())
    TWBm.start()

    TWBs = Thread(target=selector.group1, args=(selector.st1, selector.sleep))
    TWBs.start()