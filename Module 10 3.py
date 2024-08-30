import threading, random, time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.count = 0
        self.number_of_transactions = 100

    def deposit(self):
        for i in range(self.number_of_transactions):
            print('Операция по внесению денег № %s' % (i+1))
            self.count += 1
            self.money = random.randrange(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance < 500 and self.lock.locked():
                self.lock.release()
                self.balance += self.money
                self.lock.acquire()
            else:
                self.balance += self.money
            print( f'Пополнение: {self.money}. Баланс: {self.balance}.')

            #time.sleep(0.001)

    def take(self):
        for i in range(self.number_of_transactions):
            print('Операция по снятию денег № %s' %(i+1))
            self.money = random.randrange(50, 500)
            print('Запрос на: %s' %(self.money))
            if self.money <= self.balance:
                self.balance = self.balance - self.money
                print('Снятие: {}. Баланс: {}'.format(self.money, self.balance))
            elif self.count == self.number_of_transactions:
                print('Запрос отклонён, недостаточно средств, поступление средств в банкомат в ближайшее время не ожидается!')
                continue
            elif self.money > self.balance:
                print('Запрос отклонён, недостаточно средств')
                time.sleep(0.001)
                self.lock.acquire()
                #time.sleep(0.1)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))


th1.start()
th2.start()


th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
