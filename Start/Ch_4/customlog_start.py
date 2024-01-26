# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def another_function(extdata):
    logging.debug("This is a debug level message - hello world!", extra=extdata)

# set the output file and debug level, and
# TODO: use a custom formatting specification
format_str = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
extdata = {"user": "jim@example.com"}
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=format_str,
                    datefmt=datestr)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)
another_function(extdata)
