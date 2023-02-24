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
        time_min = time_sec / 60
        print("Processing time of %s(): %.2f seconds ((%.2f minutes)."
              % (func.__qualname__, time.time() - start_time, time_min))
        return result

    return measure_time
