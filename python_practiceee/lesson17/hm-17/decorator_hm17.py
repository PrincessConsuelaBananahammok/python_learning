def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Arguments: args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def get_exception(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            return result
        except Exception as e:
            print(f"Exception: {e}")
            return e
    return wrapper