import requests
responce = requests.get(url="https://jsonplaceholder.typicode.com/todos")
list1 = responce.json()
# list1 = [{'title': f'book{x}'} for x in range(1, 151)]

print(list1)

def paginator(list_obj: list, page_number=1, limit = 10) -> list:
    pages = []
    pages_temp = []
    for obg in list_obj:
        if len(pages_temp) >= limit:
            pages.append(pages_temp)
            pages_temp = []
        pages_temp.append(obg)
    print(list_obj)
    print(pages)
    print(len(pages))
    try:
        return pages[page_number - 1]
    except:
        return pages[len(pages)-1]
print(paginator(list_obj=list1, page_number=20, limit=10))
