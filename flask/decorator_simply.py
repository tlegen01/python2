import time


def decorator_before(func):
    def with_before():
        print('start action!11111111')
        func()
        print('Completed!1111111111111111')
    return with_before

@decorator_before
def write():
    print('start action!')

    print('Write file')

    print('Completed')

def read():
    print('start action!')

    print('Read file!')

    print('Completed!')


# write()
# read()
def decorator_measure_time(function):
    def decorator(*args, **kwargs): # args - позиционные (tuple(1,2,3,4)), **kwargs - именные {"key1: 12"}
        # pass
        time_start = time.perf_counter()
        result = function(*args, **kwargs)
        print(time.perf_counter() - time_start)
        return result
    return decorator
@decorator_measure_time
def tick(value: float):
    # time_start = time.perf_counter()
    # print(time_start)
    print("start tick")
    time.sleep((value))
    print('end tick')
    # print(time.perf_counter()-time_start)
    return f'completed of {value}'

result1 = tick(1.5)
# print(result1)
# result2 = tick(**{"value": 15.0})
# print(result2)
########################################
# val1 = [12, 13, 15]
# print(*val1)
# # print(type(*val1))
#
# ########################################
# def get_list(a, b, c):
#     return a, b, c
#
# res = get_list(*val1) # раскладывает массив
#########################################
# val2 = {"title": "Alisa", "surname": "ZZZZ"}
# # print(*val2)
# def get_list1(title, surname):
#     print(f"Title:{title}")
#     print(f"sername:{surname}")
# get_list1(**val2) # раскладывает словарь по титлам