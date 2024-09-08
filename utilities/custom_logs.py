import logging


class Logs:
    @staticmethod
    def get_logs():
        logging.basicConfig(filename=".\\logs\\nopCommerce.log", format='%(asctime)s:%(levelname)s:%(message)s', datefmt="%y-%m-%d %H:%M:%S", force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
