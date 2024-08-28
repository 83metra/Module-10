import threading, time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name, self.power = name, power

    def run(self):
        self.enemy, self.day_count = 100, 0
        print('{}, на нас напали!'.format(self.name))
        while self.enemy:
            self.day_count += 1
            self.enemy = self.enemy - self.power
            print(f"{self.name} сражается {self.day_count} день, осталось {self.enemy} воинов неприятеля.")
            time.sleep(1)
        else:
            print('%s одержал победу спустя %s дней(дня)!'%(self.name, self.day_count))

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

knights = [first_knight, second_knight]
for knight in knights:
    thread = knight
    thread.start()

for thread in knights:
    thread.join()
print('Все битвы закончились!')

