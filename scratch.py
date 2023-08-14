def my_decorator(func):
    def wrapper():
        print("this is happening before the function is called")
        func()
        print("this is happening after the fucnciont is called")
    return wrapper

def say_hello():
    print("Hello how are you today")

say_hello = my_decorator(say_hello)

say_hello()

say_hello()

print('-' * 100)
@my_decorator
def say_goodbye():
    print('blah blah blah')

say_goodbye()



from test import format_name, numbers

print(numbers)

# print(format_name('brian', 'stanton'))
