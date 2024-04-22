from flask import Flask, request, send_file, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    yt_link = request.form['yt_link']
    try:
        youtube_video = YouTube(yt_link)
        video = youtube_video.streams.get_highest_resolution()
        video.download(filename='video.mp4')
        return send_file('video.mp4', as_attachment=True)
    except Exception as e:
        error_message = f"Ocorreu um erro durante o download do vídeo: {str(e)}"
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
