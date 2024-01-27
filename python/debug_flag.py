import logging
import timeit


logging.getLogger().setLevel(logging.DEBUG)

s = timeit.default_timer()
if __debug__:
    logging.info("this is debug log")

logging.info("this is normal log")

print(timeit.default_timer() - s)

assert s < 0, "assert"

# python debug_flag.py
# python -O debug_flag.py