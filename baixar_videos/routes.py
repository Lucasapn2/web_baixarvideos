from flask import Flask, render_template, request, send_file, after_this_request
from pytube import YouTube
import os
from baixar_videos import app, DOWNLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    yt_link = request.form['yt_link']
    try:
        # Baixar o vídeo do YouTube
        youtube_video = YouTube(yt_link)
        video = youtube_video.streams.get_highest_resolution()

        # Definir o caminho do arquivo de vídeo
        video_file_path = os.path.join(DOWNLOAD_FOLDER, 'video.mp4')

        # Fazer o download do vídeo
        video.download(output_path=DOWNLOAD_FOLDER, filename='video.mp4')

        @after_this_request
        def remove_file(response):
            try:
                os.remove(video_file_path)
                print(f"Arquivo temporário removido: {video_file_path}")
            except Exception as e:
                print(f"Erro ao remover o arquivo temporário: {str(e)}")
            return response

        # Enviar o arquivo para o usuário
        return send_file(video_file_path, as_attachment=True, download_name='video.mp4')
    except Exception as e:
        # Log de erro e mensagem de erro
        print(f"Erro durante o download: {str(e)}")
        error_message = f"Ocorreu um erro durante o download do vídeo: {str(e)}"
        return render_template('error.html', error=error_message)

