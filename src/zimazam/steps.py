import time

def step(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Step: {func.__name__} took {end_time - start_time} seconds")
    
        return result

    return wrapper

# def intermediate_step(func: Callable, previous_result = result) -> Callable:
#     def wrapper(*args, **kwargs):

#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Step: {func.__name__} took {end_time - start_time} seconds")
    
#         return result

#     return wrapper