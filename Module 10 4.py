import queue
import threading, time, random

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
    # def __str__(self):
    #     return f'Table {self.number}'
    #
    # def say_info(self):
    #     return self.guest is None



class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        #self.time_to_eat = 0


    def run(self):
        #self.time_to_eat = (random.randint(3,10))
        #time.sleep(self.time_to_eat)
        time.sleep(random.randint(3,10))
        #for i in range (self.time_to_eat):
            #time.sleep(1)
            #print(i, sep='')

    def __str__(self):
        return self.name

class Cafe:
    threads = []
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        guests = list(guests)
        guests_count = len(list(guests))
        for i in range(len(self.tables)):
            self.tables[i].guest = guests[i]
            th = guests[i]
            self.threads.append(th)
            th.start()
            #print(f'{self.tables[i].guest} сел(-а) за стол номер {self.tables[i].number}')
            print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len(list(guests)) > len(self.tables):
            for i in range(len(self.tables), len(guests)):
                self.queue.put(guests[i])
                print('{0} в очереди'.format(guests[i]))


    def discuss_guests(self):
        while not self.queue.empty() or not self.empty_table():
        #if not self.queue.empty() and [table for table in self.tables] is not None:
            #print('Есть очередь, столы заполнены')
            for table in self.tables:
                if not (table.guest is None) and not table.guest.is_alive(): #is False:
                    print('{0} покушал(-а) и ушёл(ушла).'.format(table.guest))# + f'Стол номер {table.number} свободен')
                    #print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    #print(f'queue.get: {table.guest}')
                    #print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    th = table.guest
                    self.threads.append(th)
                    th.start()
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')



    def empty_table(self):
        for table in self.tables:
            if table.guest is None:
                return True
            else:
                return False
        #     for table in self.tables:
        #         print(table.guest)
        # else:
        #     for table in self.tables:
        #         print(table.guest)
        #     for i in range(len(self.tables)):
        #         print(f'discuss_guests: {self.tables[i]}')
        #         print(self.tables[i] is None)



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

#for table in tables:
#    print(table.say_info())

#for guest in guests:
    #print(guest)
for thread in Cafe.threads:
    thread.join()
