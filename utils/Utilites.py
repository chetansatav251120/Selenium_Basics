import logging
def get_logger():
        # Create a logger with module and optional testcase name
        logger = logging.getLogger(__name__)
        # Set log format, including testcase name if provided
        formatter = logging.Formatter(
                '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
            )
        # Create file handler to write logs to 'automation.log'
        file = logging.FileHandler("automation.log")
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger
