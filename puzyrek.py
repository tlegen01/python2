import random

list1 = [random.randint(1, 1000) for x in range(1, 100)]
print(list1)


# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

def sort_buble(list_ran: list, is_revers=False) -> list:
    len1 = len(list_ran)
    for i in range(0, len1):
        for j in range(0, len1-1-i):
            if is_revers:
                if list_ran[j] < list_ran[j + 1]:
                    # temp_i = list_ran[i]
                    # list_ran[i] = list_ran[i + 1]
                    # list_ran[i+1] = temp_i
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
            else:
                if list_ran[j] > list_ran[j + 1]:
                    list_ran[j], list_ran[j + 1] = list_ran[j + 1], list_ran[j]
    return list_ran


print(sort_buble(list1, is_revers=False))
