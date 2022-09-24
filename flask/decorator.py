import time
import requests
import threadi
import multiprocessing
import asyncio
import aiohttp

def measure(func):
    def wrap(*args, **kwargs):
        print("start measure")
        time1 = time.perf_counter()
        res = func(*args, **kwargs)
        print('end measure')
        print(f"funkciya potratila vremeni:{time.perf_counter() - time1}")
        return res
    return wrap


def download_image(name):
    response = requests.get(
        url="https://picsum.photos/370/250",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )
    # print(response)
    # print(type(response))
    #response.content #byts
    with open(f"temp/image_{name}.png", "wb") as file:
        file.write(response.content)
    return True

@measure
def sync_f():
    for i in range(1, 5):
        download_image(i)
@measure
def threading_f():
    # thread1 = threading.Thread(
    #     target = download_image,
    #     args = ('thread1',),
    #     kwargs={}
    # )
    # thread1.start()
    # thread1.join()
    thread_list = [threading.Thread(target = download_image, args = (f'thread_{x}',), kwargs={}) for x in range(1, 5)]
    # thread_list = []
    # for x in range(1, 5):
    #     thread_list.append(threading.Thread(target=download_image, args=(f'thread_{x}',), kwargs={}))
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()

@measure
def processing_f():
    # process1 = multiprocessing.Process(
    #     target = download_image,
    #     args = ('process1',),
    #     kwargs={}
    # )
    # process1.start()
    # process1.join()
    process_list = [multiprocessing.Process(target = download_image, args = (f'process_{x}',), kwargs={}) for x in range(1, 5)]
    for i in process_list:
        i.start()
    for i in process_list:
        i.join()


async def async_download_image(name):
    url = "https://picsum.photos/370/250"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url = url, headers=headers) as await_response:
            data = await await_response.read()
    with open(f"temp/image_{name}.png", "wb") as file:
        file.write(data)
    return True

@measure
def async_f():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(async_download_image("async_1"))
    async def tasks_generator(): #корутины (coro) - задачи с задержкой по выполнению и возвратуc
        await asyncio.gather(
            *[async_download_image(f"async_{x}") for x in range(1, 5)]
        )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())
    pass


#####################################################
# Загрузка тяжелой картинки
# последовательно - 1 поток, 1 процесс
# многопоточно - N поток, 1 процесс
# мультипроцесс - N поток, N процесс
# асинхронно - 1 поток, 1 процесс (цикл событий)

def tick(name):
    print(f'tick{name} start\n')
    time.sleep(1)
    print(f'tick{name} end\n')
async def tick_a(name):
    print(f'tick{name} start\n')
    await asyncio.sleep(1)
    print(f'tick{name} end\n')

@measure
def start():
    # posledovatelno
    # tick("1")
    # tick("2")
    # tick("3")
    # thread_1 = threading.Thread(target=tick, args=("thread 1",))
    # thread_1.start()
    # thread_2 = threading.Thread(target=tick, args=("thread 2",))
    # thread_2.start()
    # thread_3 = threading.Thread(target=tick, args=("thread 3",))
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()
    async def tasks_generator():  # корутины (coro) - задачи с задержкой по выполнению и возвратуc
        await asyncio.gather(
            *[tick_a(f"async_{x}") for x in range(1, 4)]
        )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


if __name__== '__main__': #точка входа, т.е. отсюда стартует этот фаил при запуске
    # sync_f()
    # threading_f()
    # processing_f()
    # async_f()
    # tick("thread")
    start()




