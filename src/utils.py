import logging
import time
from functools import lru_cache, wraps


#########################
# BENCHMARK TIME TO EXEC #
#########################
def with_benchmarking(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time} seconds to execute.")
        return result
    return wrapper

#########################
# LOGGING #
#########################
# Set up logging configuration
logging.basicConfig(level=logging.INFO) 

def with_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_message = f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}"
            
            logger = logging.getLogger(func.__module__)
            log_level = getattr(logging, level.upper())
            logger.log(log_level, log_message)
            
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

#########################
# CUSTOM CACHING WITH TTL IN SECONDS #
# SOURCE : https://stackoverflow.com/questions/31771286/python-in-memory-cache-with-time-to-live
#########################
def cache_time(max_age, maxsize=128, typed=False):
    """Least-recently-used cache decorator with time-based cache invalidation.

    Args:
        max_age: Time to live for cached results (in seconds).
        maxsize: Maximum cache size (see `functools.lru_cache`).
        typed: Cache on distinct input types (see `functools.lru_cache`).
    """
    def _decorator(fn):
        @lru_cache(maxsize=maxsize, typed=typed)
        def _new(*args, __time_salt, **kwargs):
            return fn(*args, **kwargs)

        @wraps(fn)
        def _wrapped(*args, **kwargs):
            return _new(*args, **kwargs, __time_salt=int(time.time() / max_age))

        return _wrapped

    return _decorator