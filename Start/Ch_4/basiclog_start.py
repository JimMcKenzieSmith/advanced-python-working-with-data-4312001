# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

# TODO: Try out each of the log levels
logging.debug("this is a debug level message")
logging.info("this is a debug level message")
logging.warning("this is a debug level message")
logging.error("this is a debug level message")
logging.critical("this is a debug level message")

# TODO: Output formatted strings to the log

