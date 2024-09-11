import multiprocessing, threading, datetime, time

def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as txt:
            while True:
                line = txt.readline()
                if not line: # прерывание на пустой строке
                  break
                #all_data.append(line) # целиком сырая строка
                all_data.append(line[:-1:]) # только числа, без символов переноса
    except FileNotFoundError:
        print(f'\033[31mОшибка! \033[0mФайл "{name}" не найден.\n\t Скорее всего,'
              f'Вы забыли скопировать его в каталог с программой!\n')
    # print(all_data)

if __name__ == '__main__':

    # filenames = []
    # for i in range(1,5):
    #     filenames.append(f'file {i}.txt')

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# # функции одна за другой: 0:00:05.095883
# start = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end = datetime.datetime.now()
# print(f'Время работы функций одна за другой: {end - start}')

# # время работы потоков: 0:00:05.017818
# threads = []
# start = datetime.datetime.now()
# for file in filenames:
#     th = threading.Thread(target=read_info, args = (file, ))
#     threads.append(th)
#     th.start()
#
# for th in threads:
#     th.join()
# end = datetime.datetime.now()
# print('Время работы потоков %s' %(end - start))


# многопроцессорный вызов: 0:00:01.959958
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print('Время работы многопроцессорного вызова: {}'.format(end - start))
