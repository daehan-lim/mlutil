import time


def x_y_split(dataset, class_label):
    X = dataset.iloc[:, :-1].values
    y = dataset[class_label].values
    return X, y


def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        time_sec = time.time() - start_time
        time_min = round(time_sec * 60, 2)
        print(f"Processing time of {func.__qualname__}: "
              f"{round(time.time() - start_time, 2)} sec, ({time_min} min)")
        return result

    return measure_time
