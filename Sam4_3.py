from datetime import datetime
import time

if __name__ == "__main__":
    for i in range(5):
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))  # Выводим время в формате часы:минуты:секунды
        time.sleep(1)  # Усыпляем программу на 1 секунду
