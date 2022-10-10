import multiprocessing
import threading
import time
import asyncio

import requests
import aiohttp

# def data_analyse(func):
#     def obertka(*args, **kwargs):
#         # print(args) # ('Bogdan', 'Saadat') - tuple
#         # print(type(args))
#         # print(kwargs) # {'name': 'Bogdan', 'author': 'Saadat'} - dict
#         # print(type(kwargs))
#         kwargs["author"] = kwargs["author"] + " !!!"
#         result = func(*args, **kwargs)
#
#         # Кортедж из двух элементов, где второй это длина массива
#         post_result = (result, len(result))
#         return post_result
#     return obertka
#
# @data_analyse
# def get_data(name: str, author):
#     return f"Hello {name}, {author}"
#
#
# val1 = ('Bogdan', 'Saadat')
# val2 = {'name': 'Bogdan', 'author': 'Saadat'}
#
# # data = get_data(name="Bogdan", author="Saadat")
# # data = get_data(*val1)
# data1 = get_data(**val2)
# # print(data)
# print(data1)
######################################################
# url = "https://www.gismeteo.kz/weather-nur-sultan-5164/"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/102.0.0.0 Safari/537.36'}
#
# res = requests.get(
#     url=url,
#     headers=headers)
# data = res.content # byts
# data1 = res.text # str
# # data2 = res.json
# # print(data1)
# # print(type(data1))
#
# data2 = data1.split('''class="weathertabs day-1"''') [1]
# # print(data2)
# # print(len(data2))
# # for i in data2:
# #     print(i, "\n\n\n\n\n\n\n\n\n\n\n")
#
# data3 = data2.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
# # print(data3)
# # print(len(data3))
# # for i in data3:
# #     print(i, "\n\n\n\n\n")
#
# data4 = data3[-2::1] # последние 2
# # print(data4)
# # print(type(data4))
# # print(len(data4))
#
# # day = ''
# # night = ''
# #
# # if len(data4[0]) > len(data4[1]):
# #     day = data4[0].split('''</span>''')[0]
# # else:
# #     night = data4[1].split('''</span>''')[0]
# # print(day)
# # print(night)
#
# day = ''
# night = ''
# for i in data4:
#     if len(data4[1]) == len(i):
#         day = i.split('''</span>''')[0]
#     else:
#         night = i.split('''</span>''')[0]
#
# print(f"""температура днем: {day}, а ночью {night}, город: {"https://www.gismeteo.kz/weather-nur-sultan-5164/".split('weather-')[1].split("-")[0]}""")

def time_zamer(func):
    def obertka(*args, **kwargs):
        time_start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        time_stop = time.perf_counter_ns()
        print((time_stop-time_start)//1000000, "ms") # отбросить дробную часть //
        return result
    return obertka



def get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}

    res = requests.get(
        url=url,
        headers=headers)
    data = res.content # byts
    data1 = res.text # str

    data2 = data1.split('''class="weathertabs day-1"''') [1]

    data3 = data2.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')

    data4 = data3[-2::1] # последние 2

    day = ''
    night = ''
    for i in data4:
        if len(data4[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]

    print(f"""температура днем: {day}, а ночью {night}, город: {url.split('weather-')[1].split("-")[0]}""")

city_list = [
    'https://www.gismeteo.kz/weather-nur-sultan-5164/',
    'https://www.gismeteo.kz/weather-ekibastuz-11045/',
    'https://www.gismeteo.kz/weather-pavlodar-5174/',
    'https://www.gismeteo.kz/weather-almaty-5205/',
    'https://www.gismeteo.kz/weather-kokshetau-4616/',
    'https://www.gismeteo.kz/weather-shymkent-5324/'
]

@time_zamer
def sync(): # 1 potok, 1 process
    for city in city_list:
        get_meteo(url=city)

@time_zamer
def thread(): # neskolko potokov, 1 process
    # thread1 = threading.Thread(target=get_meteo, args=('https://www.gismeteo.kz/weather-shymkent-5324/',))
    # thread1.start()
    # thread1.join()
    thread_list = []
    for city in city_list:
        new_thread = threading.Thread(target=get_meteo, args=(city,))
        thread_list.append(new_thread)
    for new_thread in thread_list:
        new_thread.start()

    for new_thread in thread_list:
        new_thread.join()
    # print(thread_list)
    # print(type(thread_list[0]))

@time_zamer
def process(): # 1 potokov, neskolko processov
    # process1 = multiprocessing.Process(target=get_meteo, args=('https://www.gismeteo.kz/weather-shymkent-5324/',))
    # process1.start()
    # process1.join()

    process_list = []
    for city in city_list:
        new_process = multiprocessing.Process(target=get_meteo, args=(city,))
        process_list.append(new_process)
    for new_process in process_list:
        new_process.start()

    for new_process in process_list:
        new_process.join()


##################################################
async def async_get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
        url=url,
        headers=headers) as response:
            res = await response.read()

    data1 = res.decode()

    data2 = data1.split('''class="weathertabs day-1"''') [1]
    data3 = data2.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
    data4 = data3[-2::1]

    day = ''
    night = ''
    for i in data4:
        if len(data4[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]

    print(f"""температура днем: {day}, а ночью {night}, город: {url.split('weather-')[1].split("-")[0]}""")

@time_zamer
def async_func():
    # for city in city_list:
    #     get_meteo(url=city)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
        *[async_get_meteo(city) for city in city_list]
        )
    )

if __name__ == "__main__":
    # sync() # 2446 ms
    # thread() # 435 ms
    # process() # 623
    async_func()
    pass


