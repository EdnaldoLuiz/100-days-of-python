import logging
import os

base_path = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_path, 'assets')
log_file = os.path.join(assets_dir, 'example.log')
utf8 = 'utf-8'

logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w', encoding=utf8)

logging.debug('Isso é uma mensagem de debug')

logging.info('Isso é uma mensagem de informação')

logging.warning('Isso é uma mensagem de aviso')

logging.error('Isso é uma mensagem de erro')

logging.critical('Isso é uma mensagem crítica')
