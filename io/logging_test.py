import logging
import logging.handlers
import os

handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "/home/centos/IdeaProjects/mp-basics/example.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

def do_something():
    logging.info("Doing something!")


do_something()
