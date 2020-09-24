import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')