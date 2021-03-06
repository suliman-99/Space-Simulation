import time
import logging

debug_mode = True


def enable_debug_mode():
    global debug_mode
    debug_mode = True
    level = logging.DEBUG
    fmt = '[%(levelname)s %(asctime)s - %(message)s]'
    logging.basicConfig(format=fmt, level=level)


def mesure_time(function, *args, **kwargs):
    start = time.perf_counter()
    function(*args, **kwargs)
    end = time.perf_counter()
    logging.debug(f'{function.__name__} takes : {end - start} seconds')
