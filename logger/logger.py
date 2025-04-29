import logging
import sys
from datetime import datetime
import colorama
from colorama import Fore, Style

class StoryLogger:
    def __init__(self):
        # Initialize colorama for Windows support
        colorama.init()
        
        # Setup logger
        self.logger = logging.getLogger('StoryTales')
        self.logger.handlers = []
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        
        # Create custom colored formatter
        class ColoredFormatter(logging.Formatter):
            FORMATS = {
                logging.INFO: Fore.GREEN + '%(levelname)s: %(message)s' + Style.RESET_ALL,
                logging.WARNING: Fore.YELLOW + '%(levelname)s: %(message)s' + Style.RESET_ALL,
                logging.ERROR: Fore.RED + '%(levelname)s: %(message)s' + Style.RESET_ALL
            }

            def format(self, record):
                log_fmt = self.FORMATS.get(record.levelno)
                formatter = logging.Formatter(log_fmt)
                return formatter.format(record)
        
        # Stream handler for console output with color
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(ColoredFormatter())
        
        # Add handler
        self.logger.addHandler(stream_handler)
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)