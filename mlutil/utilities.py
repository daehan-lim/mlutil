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
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time
