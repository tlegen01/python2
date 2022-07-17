x = lambda a: a + 10
# print(x(5))

x = lambda a, b: a * b + 10
# print(x(5, 7))

def ex_lambda(a, b):
    value = a * b + 10
    return value
print(ex_lambda(1, 2))


lst = [('candy', '30', '100'), ('apple', '10', '200'), ('baby', '20', '300')]
lst.sort(key=lambda x:x[1])
# print(lst)

# dict1 = [{'Name': 1, 'age': 2, 'quality':3}, {'apple': 2, '10': 1, '200': 3}, {'baby': 2, '20': 1, '300':3 }]
dict1 = [
    {'Name': 'A', 'age': 26, 'quality':1},
    {'Name': 'B', 'age': 20, 'quality':2},
    {'Name': "C", 'age': 33, 'quality':3},
]
# dict1.sort(key=lambda x:x["age"])
# print(dict1)

dict1.sort(key=lambda y: y["age"], reverse=True)
print(dict1)