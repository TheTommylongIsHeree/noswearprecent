import logging

# Create logger
logger = logging.getLogger('swearjar')
logger.setLevel(logging.DEBUG)  # Set to lowest level to allow all logs

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('swearjar.log')

# Set different levels for handlers
console_handler.setLevel(logging.INFO)      # Console shows INFO and above
file_handler.setLevel(logging.DEBUG)        # File shows all logs

# Create formatter and add it to handlers
log_format = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
console_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)