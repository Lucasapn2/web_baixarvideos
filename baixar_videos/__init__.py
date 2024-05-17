import os

from flask import Flask

app = Flask(__name__)
#caminho para o diretório de downloads
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')

# Certifique-se de que o diretório existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

from baixar_videos import routes