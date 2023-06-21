from datetime import datetime
from functools import wraps


def logger(old_func):

    @wraps(old_func)
    def new_func(*args, **kwargs):

        result = old_func(*args, **kwargs)

        with open('main.log', 'a') as f:
            start_time = datetime.now()
            f.write(str(start_time))
            f.write(f' | name: {old_func.__name__}')
            f.write(f' | args: {args}')
            f.write(f' | kwargs: {kwargs}')
            f.write(f' | result {type(result)}: {result}\n')

        return result

    return new_func
