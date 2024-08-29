import threading, time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name, self.power = name, power

    def run(self):
        self.enemy, self.day_count, self.day = 100, 0, ''
        print('{}, на нас напали!'.format(self.name))
        while self.enemy:
            self.day_count += 1
            self.enemy = self.enemy - self.power
            if 2 <= int(str(self.day_count)[-1]) <= 4:
                self.day = 'дня'
            elif int(str(self.day_count)[-1]) == 1:
                self.day = 'день'
            elif self.day_count > 100 and int(str(self.day_count)[-2]) in range(10, 20):
                self.day = 'дней'
            else:
                self.day = 'дней'
            print(f"{self.name} сражается {self.day_count} {self.day}, осталось {self.enemy} воинов неприятеля.")
            time.sleep(1)
        else:
            print('%s одержал победу спустя %s %s!'%(self.name, self.day_count, self.day))

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

knights = [first_knight, second_knight]
for knight in knights:
    thread = knight
    thread.start()

for thread in knights:
    thread.join()
print('Все битвы закончились, враг посрамлён и разгромлен!')
