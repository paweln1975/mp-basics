import logging
logging.basicConfig(
                    filename='/home/centos/IdeaProjects/mp-basics.py/example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s [%(levelname)-8s] %(threadName)s %(message)s',
                    datefmt='%Y.%m.%d %H:%M:%S')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')