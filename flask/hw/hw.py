import requests
import threading
import multiprocessing
import asyncio
import aiohttp


def download(doks):
    response = requests.get(
        url="https://jsonplaceholder.typicode.com/todos",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )
    # print(response.json())
    with open(f"hw/file_{doks}.json", "wb") as file:
        file.write(response.content)


def sync_f(a, b):
    for i in range(a, b):
        download(i)


def threading_f(a: int, b: int):
    thread_list = [threading.Thread(target=download, args=(f'thread_{x}',)) for x in range(a, b)]
    for i in thread_list:
        i.start()


def processing_f(a: int, b: int):
    process_list = [multiprocessing.Process(target=download, args=(f'process_{x}',), kwargs={}) for x in range(a, b)]
    for i in process_list:
        i.start()
###############################################
async def async_download_doks(doks):
    url = "https://jsonplaceholder.typicode.com/todos"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url = url, headers=headers) as await_response:
            data = await await_response.read()
    with open(f"hw/doks_{doks}.json", "wb") as file:
        file.write(data)

def async_f():
    async def tasks_generator(a: int, b: int):
        await asyncio.gather(
            *[async_download_doks(f"async_{x}") for x in range(a, b)]
        )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator(1, 10))

if __name__ == '__main__':
    # sync_f(1, 10)
    # threading_f(1, 10)
    # processing_f(1, 10)
    async_f()
