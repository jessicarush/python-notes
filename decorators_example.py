import time

def timing(func):

    """Outputs the time a function takes to execute."""

    def new_func():
        t1 = time.time()
        func()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1))
    return new_func

@timing
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)

print(my_function())
