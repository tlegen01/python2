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


write()
read()