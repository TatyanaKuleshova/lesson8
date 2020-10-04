import time
import random
import psutil
import os

#Декоратор, замеряющий время выполняемой функции

def show_time(f):

    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        stop = time.time()
        result = stop - start
        print('Времени затрачено: ' + str(result))
    return wrapper()

#Написать декоратор, замеряющий объем оперативной памяти, потребляемой декорируемой функцией

def dec_memory(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print('Используется память до выполнения функции:' + str(proc.memory_info().rss/1000000))
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        print('Память после выполнения функции:' + str(proc.memory_info().rss/1000000))
    return wrapper

#Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функции)

#Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
#натуральные числа от 1 до 1000000

@show_time
@dec_memory
def list_num():
    numbers = []
    for i in range(1000000):
        numbers.append(i)
    print('Список создан')
    return numbers

print()

@show_time
@dec_memory
def gen_list():
     for i in range(1000000):
        yield numbers





