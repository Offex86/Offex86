from flask import Flask, request, jsonify
import yt_dlp
import re

app = Flask(__name__, static_folder='static')

def get_youtube_info(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            'title': info.get('title', 'YouTube Video'),
            'thumbnail': info.get('thumbnail', ''),
            'url': info.get('url', ''),
        }

def get_instagram_info(url):
    # Note: Instagram requires advanced scraping or unofficial APIs
    return {
        'title': 'Instagram Video',
        'thumbnail': '',
        'url': url.replace("instagram.com", "ddinstagram.com")  # Example workaround
    }

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/download')
def download_video():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        if 'youtube.com' in url or 'youtu.be' in url:
            data = get_youtube_info(url)
        elif 'instagram.com' in url:
            data = get_instagram_info(url)
        else:
            return jsonify({'error': 'Unsupported platform'}), 400

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
