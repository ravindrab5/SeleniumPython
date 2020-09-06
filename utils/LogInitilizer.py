import loguru
import sys

class LogInitilizer:

    __instance = False
    __logger=None

    @staticmethod
    def getLogger():

        if not LogInitilizer.__instance:
            LogInitilizer.__instance=True
            LogInitilizer.__logger=loguru.logger
            LogInitilizer.__logger.remove()
            file_name = './info.log'
            format = "\n{level} | {time:YYYY-MM-DD at HH:mm:ss} | {name} | {function} | {line} | {message}"

            LogInitilizer.__logger.add(sink=file_name, format=format, rotation="30 days", filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='INFO')

            LogInitilizer.__logger.add(sink=sys.stdout, format=format, filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='INFO')

            LogInitilizer.__logger.add(sink=sys.stderr, format=format, filter=None,
                          colorize=None, serialize=False, backtrace=True, enqueue=True, catch=False,level='WARNING')

            LogInitilizer.__logger.info("$$$$$$  Logger initialized  $$$$$$$$$")
        return LogInitilizer.__logger