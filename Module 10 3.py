import threading, random, time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock

    def deposit(self):
        for i in range(10):
            self.money = random.randrange(50, 500)
            self.balance += self.money
            print(self.lock)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print( f'Пополнение: {self.money}. Баланс: {self.balance}.')

    def take(self):
        for i in range(10):
            self.money = random.randrange(50, 500)
            print('Запрос на: %s' %(self.money))
            if self.money <= self.balance:
                self.balance = self.balance - self.money
                print('Снятие: {}. Баланс: {}'.format(self.money, self.balance))
            elif self.money > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))


th1.start()
th2.start()


th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')