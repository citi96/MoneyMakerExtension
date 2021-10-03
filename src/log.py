import logging
import os
import datetime as dt

<<<<<<< HEAD

=======
>>>>>>> 428d54f04d4d4d8833cd00677ce8274d40eea03d
class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

<<<<<<< HEAD

=======
>>>>>>> 428d54f04d4d4d8833cd00677ce8274d40eea03d
# python 3 style
class MyLogger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
<<<<<<< HEAD
        formatter = logging.Formatter(
            "%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s"
        )
=======
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')
>>>>>>> 428d54f04d4d4d8833cd00677ce8274d40eea03d

        now = dt.datetime.now()
        dirname = "./log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
<<<<<<< HEAD
        fileHandler = logging.FileHandler(
            dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log"
        )
=======
        fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")
>>>>>>> 428d54f04d4d4d8833cd00677ce8274d40eea03d

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        print("Generate new instance")

    def get_logger(self):
<<<<<<< HEAD
        return self._logger
=======
        return self._logger
>>>>>>> 428d54f04d4d4d8833cd00677ce8274d40eea03d
