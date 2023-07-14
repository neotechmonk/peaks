import logging
import time


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



