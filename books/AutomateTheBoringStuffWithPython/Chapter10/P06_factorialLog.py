# This program calculates factorial and logs debug messages

import logging
#logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # log to terminal
logging.basicConfig(filename="factorialLog.txt", level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s")  # optional log to file
logging.disable(logging.CRITICAL)  # Stop logging, comment out to debug
logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial(%s%%)" % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug("End of factorial(%s%%)" % n)
    return total


print(factorial(5))
logging.debug("End of program")
