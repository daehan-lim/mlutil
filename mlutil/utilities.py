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
        time_sec = round(time.time() - start_time, 3)
        time_min = round(time_sec * 60, 3)
        print(f"Processing time of {func.__qualname__}: "
              f"{time_sec} sec, ({time_min} min)")
        return result

    return measure_time
