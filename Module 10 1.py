import threading, datetime, os.path, time

def write_words(word_count, file_name):
    number = 1
    if os.path.isfile(file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in range(word_count):
                file.write('Какое-то слово № %s\n' %(number))
                number += 1
                time.sleep(0.1)
    else:
        with open(file_name, 'w+', encoding='utf-8') as file:
            for line in range(word_count):
                file.write('Какое-то слово № %s\n' %(number))
                number += 1
                time.sleep(0.1)
    print('Завершилась запись в файл {0}'.format(file_name))

time_start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.datetime.now()
print('Поочерёдная запись заняла {} секунд'.format(time_end-time_start))

erster_schreiber = threading.Thread(target=write_words, args=(10, 'example5.txt'))
zweiter_schreiber = threading.Thread(target=write_words, args=(30, 'example6.txt'))
dritter_schreiber = threading.Thread(target=write_words, args=(200, 'example7.txt'))
vierter_schreiber = threading.Thread(target=write_words, args=(100, 'example8.txt'))

time_start = datetime.datetime.now()
erster_schreiber.start()
zweiter_schreiber.start()
dritter_schreiber.start()
vierter_schreiber.start()

erster_schreiber.join()
zweiter_schreiber.join()
dritter_schreiber.join()
vierter_schreiber.join()
time_end = datetime.datetime.now()
print(f'Работа потоков {time_end-time_start} секунд')