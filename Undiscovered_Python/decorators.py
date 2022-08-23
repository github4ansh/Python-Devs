import functools
import time


def calculate_execution_time_of_function(func):

    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'STARTING TIME: function: {func} with argument as: {func.__name__}({kwargs["name"]})')
        st = time.perf_counter()
        output = func(*args, **kwargs)
        time.sleep(2)
        et = time.perf_counter()
        print(f'FINISHING TIME: function: {func} with argument as: {func.__name__}({kwargs["name"]})')
        print(f'Total elapsed time for execution of function: {round(et - st, 2)} secs.')
        return output
    return wrapper


def callable_logger(func):

    @functools.wraps(func)
    def pass_name_wrapper(*args, **kwargs):
        print(f'START LOG: function: {func} with argument as: {func.__name__}({kwargs["name"]})')
        output = func(*args, **kwargs)
        print(f'FINISH LOG: function: {func} with argument as: {func.__name__}({kwargs["name"]})')
        return output
    return pass_name_wrapper


@calculate_execution_time_of_function
@callable_logger
def greet(name):
    """
    Function greets a person with the given name

    :param: Greeting Person's Name
    :return: Greet Message
    """
    return f'Welcome to programming world, {name}'


person_name = 'Twitch'
print(greet(name=person_name))